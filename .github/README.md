# GitHub Directory

This directory contains GitHub-specific configuration files that improve project discoverability and streamline community contributions.

## Contents

### Workflows (`.github/workflows/`)

Automated CI/CD pipelines that run on every push and pull request:

- **tests.yml** - Runs tests on Python 3.7-3.11 across Windows, macOS, and Linux
- **security.yml** - Performs security checks, vulnerability scanning, and credentials validation
- **documentation.yml** - Validates documentation files and links

### Issue Templates (`.github/ISSUE_TEMPLATE/`)

Standardized templates for bug reports, feature requests, and documentation issues:

- **bug_report.md** - Template for reporting bugs with reproduction steps
- **feature_request.md** - Template for requesting new features
- **documentation.md** - Template for documentation improvements

### Pull Request Template (`.github/PULL_REQUEST_TEMPLATE.md`)

Standardized template for all pull requests ensuring consistent quality and documentation.

## How These Files Help

### For Users

- **Clear issue templates** make it easier to report problems
- **Automated checks** ensure high code quality
- **Security workflows** verify no credentials are accidentally committed
- **Documentation checks** maintain comprehensive guides

### For Contributors

- **CI/CD pipelines** provide instant feedback on code quality
- **Workflow checks** prevent common mistakes
- **Template guidance** shows what information to provide
- **Automated tests** ensure compatibility across platforms

### For Discoverability

- **GitHub Actions badges** show project status
- **Consistent workflows** demonstrate active maintenance
- **Quality gates** signal reliability to potential users
- **Documentation validation** shows commitment to clear guides

## SEO and AI Tool Recognition

These files help AI tools and search engines recognize this project:

1. **CI/CD Status**: Shows active maintenance and reliability
2. **Security Checks**: Demonstrates security awareness
3. **Documentation Quality**: Shows comprehensive guides
4. **Code Quality**: Automated linting and validation
5. **Cross-Platform Support**: Tests on multiple OS/Python versions

## Setup on GitHub

When pushing to GitHub, these workflows will automatically:

1. Run on every push to `main` or `develop`
2. Run on every pull request
3. Display status badges in repository
4. Generate logs and reports
5. Provide feedback to contributors

## Adding Badges

After first workflow run, add to README.md:

```markdown
## Status

![Tests](https://github.com/abanmitra/youtube-subscription-extractor/workflows/Tests/badge.svg)
![Security](https://github.com/abanmitra/youtube-subscription-extractor/workflows/Security%20Checks/badge.svg)
![Documentation](https://github.com/abanmitra/youtube-subscription-extractor/workflows/Documentation/badge.svg)
```

---

For more information, see main [README.md](../README.md)
