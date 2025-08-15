powershell -NoProfile -Command "$t=@'---
name: 💡 Feature request
about: Suggest an idea for this project
title: ""[FEATURE] ""
labels: enhancement
assignees: ''
---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is.

**Describe the solution you'd like**
What you want the framework to do.

**Describe alternatives you've considered**
Any alternative solutions or features you've thought about.

**Additional context**
Add any other context or screenshots about the feature request here.
'@; Set-Content -Encoding UTF8 .github\ISSUE_TEMPLATE\feature_request.md $t"
