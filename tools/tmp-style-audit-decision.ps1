$files = @(
  "decision-source/knowledge/common/component-decision.md",
  "decision-source/knowledge/common/layout-decision.md"
)

$patterns = @(
  "这里的",
  "这套",
  "这页",
  "后续",
  "默认",
  "优先",
  "应先",
  "不再优先",
  "不按普通弹窗",
  "仅作为",
  "不是单个组件页",
  "强坐标",
  "基线"
)

foreach ($file in $files) {
  "FILE: $file"
  $lines = Get-Content $file
  for ($i = 0; $i -lt $lines.Length; $i++) {
    foreach ($pattern in $patterns) {
      if ($lines[$i] -like "*$pattern*") {
        "{0}:{1}" -f ($i + 1), $lines[$i]
        break
      }
    }
  }
  "----"
}
