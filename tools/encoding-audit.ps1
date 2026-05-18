[CmdletBinding()]
param(
  [string[]]$Extensions = @('*.md', '*.json', '*.txt', '*.yml', '*.yaml', '*.js', '*.ts', '*.html', '*.css'),
  [switch]$AsJson
)

$strictUtf8 = [System.Text.UTF8Encoding]::new($false, $true)

function Get-TargetFiles {
  $args = @('--files')
  foreach ($ext in $Extensions) {
    $args += '-g'
    $args += $ext
  }

  $paths = & rg @args
  if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne 1) {
    throw 'rg --files failed'
  }

  return $paths
}

function Test-SuspiciousMojibake {
  param(
    [string]$Text
  )

  $cpC3 = [string][char]0x00C3
  $cpC2 = [string][char]0x00C2
  $cpE2 = [string][char]0x00E2

  return (
    $Text -match ([regex]::Escape($cpC3) + '.') -or
    $Text -match ([regex]::Escape($cpC2) + '.') -or
    $Text -match ([regex]::Escape($cpE2) + '..')
  )
}

$rows = foreach ($path in Get-TargetFiles) {
  $fullPath = (Resolve-Path $path).Path
  $bytes = [System.IO.File]::ReadAllBytes($fullPath)
  $hasBom = $bytes.Length -ge 3 -and
    $bytes[0] -eq 0xEF -and
    $bytes[1] -eq 0xBB -and
    $bytes[2] -eq 0xBF

  $utf8Valid = $true
  $text = $null
  try {
    $text = $strictUtf8.GetString($bytes)
  } catch {
    $utf8Valid = $false
  }

  $hasReplacementChar = $utf8Valid -and $text.Contains([char]0xFFFD)
  $hasSuspiciousMojibake = $utf8Valid -and (Test-SuspiciousMojibake -Text $text)
  $matchesPolicy = $utf8Valid -and $hasBom

  $classification = if (-not $utf8Valid -or $hasReplacementChar) {
    'B:on-disk-encoding-damage'
  } elseif ($hasSuspiciousMojibake) {
    'C:manual-review'
  } else {
    'A:display-path-issue-or-normal'
  }

  $recommendedAction = if (-not $utf8Valid -or $hasReplacementChar) {
    'repair-content'
  } elseif (-not $hasBom) {
    'rewrite-as-utf8-bom'
  } elseif ($hasSuspiciousMojibake) {
    'manual-review'
  } else {
    'no-rewrite-policy-compliant'
  }

  [pscustomobject]@{
    Path = $path
    Extension = [System.IO.Path]::GetExtension($path)
    Utf8Valid = $utf8Valid
    Utf8Bom = $hasBom
    MatchesPolicy = $matchesPolicy
    HasReplacementChar = $hasReplacementChar
    SuspiciousMojibake = $hasSuspiciousMojibake
    Classification = $classification
    RecommendedAction = $recommendedAction
    Size = $bytes.Length
  }
}

if ($AsJson) {
  $rows | ConvertTo-Json -Depth 4
} else {
  $rows | Sort-Object Path | Format-Table -AutoSize
}
