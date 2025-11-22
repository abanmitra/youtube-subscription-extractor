# Contributing to YouTube Subscription Extractor

Thank you for your interest in contributing to this **YouTube subscription extraction tool**! This document provides comprehensive guidelines and instructions for contributing to this open-source project.

Whether you're fixing bugs, adding features, improving documentation, or enhancing the YouTube API integration, your contributions help make this subscription backup and analysis tool better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

This project adheres to a Contributor Code of Conduct. By participating, you are expected to uphold this code. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

## How Can I Contribute to YouTube Subscription Extractor?

### Reporting Bugs & Issues

Before submitting a bug report:
1. Check the [issue tracker](https://github.com/abanmitra/youtube-subscription-extractor/issues)
2. Review the [TROUBLESHOOTING.md](TROUBLESHOOTING.md) guide

**When reporting bugs, include:**
- Clear, descriptive title
- Python version and OS
- Exact steps to reproduce
- Current behavior and expected behavior
- Error messages or logs
- Your environment details

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
1. Use a clear, descriptive title
2. Provide a detailed description
3. Explain the benefits
4. List any alternatives considered
5. Include examples if applicable

### Code Contributions

We welcome pull requests for:
- Bug fixes
- New features
- Documentation improvements
- Test coverage expansion
- Performance improvements

## Development Setup

### Prerequisites

- Python 3.7 or higher
- Git
- GitHub account

### Local Development

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/youtube-subscription-extractor.git
   cd youtube-subscription-extractor
   ```

3. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Testing Your Changes

Before submitting:
1. Test the application manually with your setup
2. Verify all features still work
3. Check error handling
4. Test with multiple accounts if modifying core logic

## Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) conventions
- Use 4 spaces for indentation
- Use meaningful variable and function names
- Keep lines under 88 characters when possible
- Add docstrings to all functions and classes

### Docstring Format

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of what the function does.
    
    Longer description explaining the function's behavior,
    parameters, and return value if needed.
    
    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2
    
    Returns:
        bool: Description of return value
    
    Raises:
        ValueError: When input validation fails
    """
    pass
```

### Comments

- Use comments to explain "why", not "what"
- Keep comments clear and concise
- Update comments if code changes

### Type Hints

Use type hints for better code clarity:
```python
from typing import Dict, List, Any

def process_data(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """Process data and return summary statistics."""
    pass
```

## Commit Messages

Follow these guidelines for clear, readable commit history:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring without feature/fix changes
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples

Good:
```
feat(auth): add token refresh mechanism

Implement automatic token refresh when access token expires.
Tokens are now refreshed silently without requiring re-authentication.

Fixes #123
```

```
fix(csv_handler): handle special characters in channel names

Special characters in CSV headers were causing parsing errors.
Now properly escaping and quoting headers.

Fixes #456
```

### Guidelines

- Use imperative mood ("add feature" not "added feature")
- Don't capitalize the subject
- Don't end subject with a period
- Wrap body at 72 characters
- Reference related issues with "Fixes #XXX" or "Relates to #XXX"

## Pull Request Process

### Before Submitting

1. **Update your branch**
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Run your changes**
   ```bash
   python src/youtube_extractor.py
   ```

3. **Verify no sensitive data**
   ```bash
   git diff
   ```

### Creating a Pull Request

1. Push your branch to your fork
2. Go to the original repository
3. Click "New Pull Request"
4. Select your fork and branch
5. Fill in the PR template with:
   - Clear description of changes
   - Related issues (if any)
   - Testing performed
   - Any breaking changes

### PR Requirements

- [ ] Code follows style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex logic
- [ ] No new warnings generated
- [ ] Tests added/updated (if applicable)
- [ ] Documentation updated
- [ ] No sensitive data in commits
- [ ] Commit messages follow guidelines

### Responding to Reviews

- Respond to all feedback
- Request re-review after changes
- Be respectful and professional
- Ask for clarification if needed
- Appreciate reviewer's time and effort

## Reporting Issues

### Security Issues

**Do NOT** open public issues for security vulnerabilities.

Email: abanmitra@gmail.com with:
- Description of vulnerability
- Steps to reproduce (if possible)
- Potential impact
- Suggested fix (if any)

### Bug Reports

Use the [GitHub issue tracker](https://github.com/abanmitra/youtube-subscription-extractor/issues):

1. Click "New Issue"
2. Choose "Bug Report"
3. Fill in all sections
4. Submit

### Feature Requests

1. Click "New Issue"
2. Choose "Feature Request"
3. Describe desired functionality
4. Explain use cases and benefits

## Development Tips

### Debug Mode

Add to your code to enable debugging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Testing Multiple Accounts

Use test accounts or secondary Gmail accounts when testing:
1. Create test Google account
2. Add to OAuth test users
3. Add email to `youtube_accounts.csv`
4. Test the full flow

### Checking Changes

```bash
# See what changed
git diff

# See staged changes
git diff --staged

# See commit history
git log --oneline

# See status
git status
```

## Questions?

- Check [README.md](README.md) for basic usage
- Review [SECURITY.md](SECURITY.md) for security topics
- Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues
- Review existing [issues](https://github.com/abanmitra/youtube-subscription-extractor/issues)

---

**Thank you for contributing to YouTube Subscription Extractor!** 🎉

Your contributions make this project better for everyone.
