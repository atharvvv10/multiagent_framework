powershell -NoProfile -Command "$t=@'# 📌 Pull Request

## Description
Describe the changes you’ve made.

## Related Issue
Closes # (issue number)

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactor

## Checklist
- [ ] Code follows the style guidelines
- [ ] Self-reviewed the code
- [ ] Added comments where necessary
- [ ] No new warnings
- [ ] Added tests (if applicable)
- [ ] All tests pass
'@; Set-Content -Encoding UTF8 .github\PULL_REQUEST_TEMPLATE.md $t"
