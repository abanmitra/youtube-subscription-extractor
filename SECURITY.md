# Security & Best Practices

Comprehensive guide for protecting sensitive data and secure usage of the YouTube Subscription Extractor application.

## Overview

This application handles OAuth credentials and authentication tokens. This document explains how your data is protected and provides best practices for secure usage.

## Sensitive Data Protection

### File Organization

The application uses dedicated folders to organize sensitive and generated files:

```
secret/                    ← ALL SENSITIVE FILES (keep private)
├── credentials_config.json
└── token_*.pickle

output/                    ← Generated data (local use)
├── merged_channels.csv
└── channels_*.csv

src/                       ← Application code (safe to share)
├── youtube_merger.py
├── auth.py
├── youtube_api.py
└── csv_handler.py
```

## Key Files

### credentials_config.json

**Location**: `secret/credentials_config.json`

**What it contains**: OAuth client credentials from Google Cloud Console

**Security level**: CRITICAL

**Protection**:
- Never share this file
- Never upload to version control
- Keep in `secret/` folder only
- Delete and regenerate if compromised

**If compromised**:
1. Go to Google Cloud Console → Credentials
2. Delete the compromised OAuth client
3. Create a new OAuth client
4. Download and replace the file

### Authentication Tokens

**Location**: `secret/token_[email].pickle`

**What they contain**: Encrypted access tokens for each account

**Security level**: HIGH

**Protection**:
- Never share token files
- Automatically created on first authentication
- Stored in `secret/` folder
- Protected by `.gitignore`

**If compromised**:
1. Delete the `token_[email].pickle` file
2. Run the application again to re-authenticate
3. New token is created automatically

### youtube_accounts.csv

**Location**: `youtube_accounts.csv` (root directory)

**What it contains**: Email addresses of YouTube accounts

**Security level**: MEDIUM

**Protection**:
- Treat as confidential
- Protected by `.gitignore`
- Keep locally only

## Security Best Practices

### Before First Run

- ✅ Downloaded OAuth credentials from Google Cloud Console
- ✅ Renamed file to `credentials_config.json`
- ✅ Placed in `secret/` folder (NOT root)
- ✅ Did NOT upload credentials to any public location
- ✅ Did NOT share credentials file with anyone

### During Usage

- ✅ Never commit `secret/` folder to Git
- ✅ Never share `secret/` folder
- ✅ Never upload to cloud storage services
- ✅ Keep YouTube account passwords secure
- ✅ Use 2FA on your Google account

### If Sharing Source Code

Share ONLY these files:
- `src/` folder (application code)
- `requirements.txt`
- `README.md`
- `SECURITY.md`
- `.gitignore`

Do NOT share:
- `secret/` folder
- `youtube_accounts.csv`
- `output/` folder

### Git/Version Control

Configure your `.gitignore` to prevent accidental commits:

```
# Sensitive data
secret/
credentials_config.json
youtube_accounts.csv

# Generated files
output/

# Python cache
__pycache__/
*.pyc
*.pyo
*.egg-info/
```

Before committing, verify nothing sensitive is staged:
```bash
git status
```

## OAuth 2.0 Security

### Why OAuth (Not Passwords)

Benefits of OAuth:
- Your passwords are NEVER shared with the application
- The application cannot store your passwords
- You control exactly what permissions are granted
- Access can be revoked instantly
- Complies with security best practices

### Scope Limitation

This application uses only `youtube.readonly` scope:
- Read-only access to subscriptions
- Cannot modify or delete subscriptions
- Cannot access private videos
- Cannot access watch history

## Token Management

### Token Lifecycle

1. **First Authentication**: Browser opens for login → Token created and saved
2. **Subsequent Runs**: Token loaded from `secret/` folder → Used automatically
3. **Token Expiration**: Tokens expire after ~1 hour → Auto-refreshed
4. **Force Re-authentication**: Delete token file → Run application → New login

### Token Refresh

Tokens are automatically managed by the application:
- Access tokens expire after ~1 hour
- Refresh tokens last longer (~6 months)
- Automatic refresh happens without user interaction
- No manual token management needed

## Common Security Mistakes to Avoid

### DON'T

- ❌ Put `credentials_config.json` in root directory
- ❌ Commit `secret/` folder to Git
- ❌ Email credentials to anyone
- ❌ Upload credentials to cloud storage (Dropbox, OneDrive, etc.)
- ❌ Share entire `secret/` folder
- ❌ Post credentials on forums or Stack Overflow
- ❌ Use same credentials for multiple applications
- ❌ Store passwords alongside credentials

### DO

- ✅ Store credentials in `secret/` folder
- ✅ Use `.gitignore` to protect sensitive files
- ✅ Share only source code files
- ✅ Keep credentials locally on your machine
- ✅ Delete tokens if you stop using the application
- ✅ Review Google Cloud Console regularly
- ✅ Create separate OAuth clients if needed
- ✅ Keep Google account secure (2FA, strong password)

## Security Incident Response

### Credentials Compromised

**Immediate (within 5 minutes)**:
1. Go to Google Cloud Console
2. Find your OAuth client in Credentials
3. Delete it immediately

**Follow-up (within 30 minutes)**:
1. Create new OAuth client
2. Download new credentials
3. Replace `secret/credentials_config.json`
4. Delete all token files from `secret/`
5. Run application to re-authenticate

### Token Compromised

**Immediate**:
1. Delete: `secret/token_[email].pickle`
2. Run: `python src\youtube_merger.py`
3. Re-authenticate when prompted

**Follow-up**:
1. Check account activity in Google Security
2. Review for suspicious access
3. Enable 2FA if not already enabled

## Permissions and Access

### What the Application Can Access

- ✅ List of subscribed channels
- ✅ Channel names and metadata
- ✅ Channel categories
- ✅ Public channel information

### What the Application CANNOT Access

- ❌ Your passwords
- ❌ Private videos
- ❌ Watch history
- ❌ Liked videos
- ❌ Saved playlists
- ❌ Personal data beyond subscriptions
- ❌ Other accounts' information

## Local Data Storage

All data remains on your local machine:
- ✅ Credentials stored locally in `secret/`
- ✅ Tokens stored locally in `secret/`
- ✅ CSV files generated locally in `output/`
- ✅ Nothing uploaded to external servers
- ✅ Nothing sent to project repository
- ✅ Complete data control

## Regular Security Audits

### Monthly

- [ ] Check Google Cloud Console for unexpected OAuth clients
- [ ] Review recent activity in your Google account
- [ ] Verify credentials are in `secret/` folder
- [ ] Check `.gitignore` is properly configured

### Quarterly

- [ ] Review this security guide
- [ ] Audit all files in `secret/` folder
- [ ] Check for any accidentally committed sensitive files
- [ ] Verify access logs if available

## Testing Your Setup

### Verify Credentials Protection

```bash
# Check credentials file exists in correct location
Test-Path "secret/credentials_config.json"

# Check file is not committed to Git
git check-ignore secret/credentials_config.json
```

### Verify Git Protection

```bash
# Check .gitignore is configured
type .gitignore

# Verify sensitive files are ignored
git status
```

## Additional Resources

### Google Cloud Security

- [Google Cloud Security Best Practices](https://cloud.google.com/security/best-practices)
- [Google Cloud Console](https://console.cloud.google.com/)
- [OAuth 2.0 Protocol](https://tools.ietf.org/html/rfc6749)

### YouTube API

- [YouTube Data API v3 Documentation](https://developers.google.com/youtube/v3)
- [YouTube API Authentication Guide](https://developers.google.com/youtube/v3/getting-started)

### Security Standards

- [OWASP Security Guidelines](https://owasp.org/)
- [API Security Best Practices](https://cheatsheetseries.owasp.org/cheatsheets/API_Security_Cheat_Sheet.html)

### Account Security

- [Google Account Security Checkup](https://myaccount.google.com/security-checkup)
- [Two-Factor Authentication Setup](https://myaccount.google.com/security)

## Questions or Issues?

Refer to:
1. This security guide for protection strategies
2. README.md for setup and usage instructions
3. Error messages in console output
4. Google Cloud Console documentation

---

**Important**: Always prioritize security. If you're unsure about any step, err on the side of caution.

**Last Updated**: November 2025
