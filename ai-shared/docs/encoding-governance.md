# XGame Encoding Governance

## Policy

- Repository text files use UTF-8 with BOM.
- Repository text files use LF line endings.
- The policy applies to `.md`, `.json`, `.txt`, `.yml`, `.yaml`, `.js`, `.ts`, `.html`, and `.css`.
- This repository intentionally prefers BOM because Windows PowerShell 5.1 and related Windows tooling are primary consumers during authoring and audit.

## Classification

- `A: display-path issue`
  A file is valid UTF-8 and renders correctly when read explicitly as UTF-8. Garbling appears only through default terminal settings, default `Get-Content`, or inconsistent code-page/output settings.
- `B: on-disk encoding damage`
  A file is not strict UTF-8, or it remains mojibake after strict UTF-8 decode, or it is confirmed against a trusted source to have been written with corrupted text.
- `C: manual review`
  A file is valid UTF-8 but its semantic correctness cannot be proven automatically.

## PowerShell Guidance

- In Windows PowerShell 5.1, BOM-bearing UTF-8 files are treated more reliably by default than UTF-8 files without BOM.
- Prefer explicit UTF-8 reads when auditing text files, but the repository default now aims to keep even default `Get-Content` behavior stable.
- If terminal output itself is suspicious, verify at the byte level before rewriting any file.

## Audit Entry Point

- Use `tools/encoding-audit.ps1` for a repeatable read-only audit.
- The script reports strict UTF-8 validity, BOM presence, suspicious mojibake patterns, and a recommended action.

## Repair Rules

- Do not batch-rewrite the repository only to normalize encoding.
- Only rewrite files when one of these is true:
  - the file contains confirmed on-disk corruption
  - the file is a narrow style exception that needs normalization, such as a UTF-8 without BOM file in this UTF-8 with BOM repository
- When rewriting for normalization only, preserve content exactly and verify that the only byte-level change is the added BOM or line-ending normalization that was explicitly intended.
