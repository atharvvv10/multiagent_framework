powershell -NoProfile -Command "$t=@'---
name: 🐞 Bug report
about: Report a bug to help us improve
title: ""[BUG] ""
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description of the issue.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Run '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain.

**Environment (please complete the following):**
 - OS: [e.g. Windows 11]
 - Python Version: [e.g. 3.10]
 - Branch: [e.g. main]

**Additional context**
Add any other context about the problem here.
'@; Set-Content -Encoding UTF8 .github\ISSUE_TEMPLATE\bug_report.md $t"
