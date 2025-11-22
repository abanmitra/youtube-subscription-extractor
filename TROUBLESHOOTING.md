# Troubleshooting Guide

Common issues and solutions for the YouTube Subscription Extractor.

## Table of Contents

- [Authentication Issues](#authentication-issues)
- [API Issues](#api-issues)
- [File and Path Issues](#file-and-path-issues)
- [Data Export Issues](#data-export-issues)
- [Network and Connection Issues](#network-and-connection-issues)
- [Performance Issues](#performance-issues)
- [Advanced Troubleshooting](#advanced-troubleshooting)

## Authentication Issues

### "Credentials config file not found"

**Error Message:**
```
Error: Credentials config file not found at secret/credentials_config.json
```

**Causes:**
- File not downloaded from Google Cloud Console
- Wrong filename
- Wrong location
- File was deleted

**Solutions:**

1. **Verify file exists:**
   ```bash
   # Windows
   Test-Path "secret/credentials_config.json"
   
   # Mac/Linux
   test -f secret/credentials_config.json && echo "Found" || echo "Not found"
   ```

2. **Check file location:**
   - Should be at: `secret/credentials_config.json` (NOT in root)
   - Verify folder structure exists

3. **Re-download credentials:**
   - Go to Google Cloud Console
   - Navigate to APIs & Services → Credentials
   - Find your OAuth client
   - Click download icon
   - Rename to `credentials_config.json`
   - Place in `secret/` folder

4. **Create secret folder if missing:**
   ```bash
   # Windows
   mkdir secret
   
   # Mac/Linux
   mkdir -p secret
   ```

### "OAuth Access Denied"

**Error Message:**
```
Error: Access denied. User not in test users list.
```

**Causes:**
- Account email not added as Test User in Google Cloud Console
- OAuth consent screen not configured
- Credentials expired or invalid

**Solutions:**

1. **Add account as Test User:**
   - Go to Google Cloud Console
   - OAuth consent screen
   - Add Testing → Add users
   - Enter the email address being used
   - Save

2. **Verify consent screen settings:**
   - OAuth consent screen should be configured
   - App name, user support email, etc. filled in

3. **Wait for propagation:**
   - Changes may take 5-10 minutes
   - Try again after waiting

4. **Re-authenticate:**
   ```bash
   # Delete the token file
   # Windows
   Remove-Item "secret/token_[email].pickle"
   
   # Mac/Linux
   rm secret/token_[email].pickle
   ```
   - Run the script again
   - Sign in with your account

5. **Use correct email:**
   - Email in `youtube_accounts.csv` must match Google account email
   - Check for typos or extra spaces

### "Invalid Credentials"

**Error Message:**
```
Error: The OAuth client ID is invalid
```

**Causes:**
- Credentials JSON corrupted
- Downloaded credentials from wrong project
- OAuth client was deleted

**Solutions:**

1. **Verify credentials file:**
   ```bash
   # Try opening with text editor
   # Should contain: client_id, client_secret, redirect_uris
   ```

2. **Check OAuth client still exists:**
   - Google Cloud Console → Credentials
   - Verify "Desktop application" OAuth client exists

3. **Regenerate credentials:**
   - Delete current credentials from Console
   - Create new OAuth client
   - Download and replace file

### "Token Expired"

**Error Message:**
```
Error: Token has expired and cannot be refreshed
```

**Causes:**
- Token too old (hasn't been used in ~6 months)
- Manual deletion of tokens
- System clock wrong

**Solutions:**

1. **Delete expired token:**
   ```bash
   # Windows
   Remove-Item "secret/token_[email].pickle"
   
   # Mac/Linux
   rm secret/token_[email].pickle
   ```

2. **Run script again:**
   - New token will be created
   - Browser will open for re-authentication

3. **Check system clock:**
   - Incorrect system time can cause token issues
   - Sync system clock with internet time

## API Issues

### "YouTube Data API is not enabled"

**Error Message:**
```
Error: YouTube Data API v3 is not enabled for this project
```

**Causes:**
- API not enabled in Google Cloud Console
- Enabled on wrong project
- Takes time to activate

**Solutions:**

1. **Enable the API:**
   - Go to Google Cloud Console
   - Select correct project (check project dropdown)
   - APIs & Services → Library
   - Search for "YouTube Data API v3"
   - Click "Enable"

2. **Wait for activation:**
   - Takes 5-10 minutes sometimes
   - Wait and try again

3. **Verify project selection:**
   - Ensure you're in the correct Google Cloud project
   - Check project name in console header

4. **Check quota:**
   - APIs & Services → Quotas
   - Verify YouTube Data API has quota available

### "Quota Exceeded"

**Error Message:**
```
Error: The request quota has been exceeded
```

**Causes:**
- API quota exceeded for the day
- Too many requests in short time
- Development project has low quota

**Solutions:**

1. **Wait and retry:**
   - Quotas reset daily at midnight PT
   - Try again tomorrow

2. **Upgrade to higher quota:**
   - Request quota increase in Google Cloud Console
   - Takes 24-48 hours to process

3. **Optimize requests:**
   - Don't run multiple instances simultaneously
   - Batch requests when possible

4. **Check current usage:**
   - APIs & Services → Quotas
   - View daily usage statistics

### "Permission Denied"

**Error Message:**
```
Error: Permission denied on resource youtube
```

**Causes:**
- OAuth scopes incorrect
- Account doesn't have YouTube access
- Channel made private

**Solutions:**

1. **Verify OAuth scopes:**
   - Code should use `youtube.readonly` scope
   - Credentials should have YouTube permission

2. **Check account status:**
   - Ensure account has YouTube access
   - YouTube may be disabled for certain account types

3. **Re-authenticate:**
   - Delete token file
   - Run script again
   - Grant permissions when prompted

4. **Check channel settings:**
   - Ensure subscriptions are not private
   - Go to YouTube settings → Privacy

## File and Path Issues

### "youtube_accounts.csv not found"

**Error Message:**
```
Error: Cannot find youtube_accounts.csv
```

**Causes:**
- File not created
- Wrong filename
- File in wrong location
- File deleted

**Solutions:**

1. **Create the file:**
   ```csv
   username
   user1@gmail.com
   user2@gmail.com
   ```
   - Save as `youtube_accounts.csv`
   - Place in project root directory

2. **Check file location:**
   - Should be at project root, not in subfolder
   - Windows: `D:\work\youtube\youtube_accounts.csv`

3. **Verify file format:**
   - Must be CSV format
   - First line must be: `username`
   - One email per line after header

4. **Check file permissions:**
   - File should be readable
   - Check Windows/Unix permissions

### "Output directory cannot be created"

**Error Message:**
```
Error: Cannot create output directory
```

**Causes:**
- Permission denied
- Path too long
- Invalid path characters
- Disk full

**Solutions:**

1. **Check permissions:**
   ```bash
   # Windows
   icacls output
   
   # Mac/Linux
   ls -la | grep output
   ```

2. **Manual directory creation:**
   ```bash
   # Windows
   mkdir output
   
   # Mac/Linux
   mkdir -p output
   ```

3. **Check disk space:**
   ```bash
   # Windows
   Get-Volume
   
   # Mac/Linux
   df -h
   ```

4. **Use different path:**
   - If permissions issue, move project to different location
   - Try: C:\ or user home directory

### "File already exists"

**Error Message:**
```
Warning: File already exists. Overwriting...
```

**Causes:**
- Running script multiple times
- Previous export still exists
- Naming collision

**Solutions:**

1. **This is normal:**
   - Script will overwrite old files
   - This is expected behavior

2. **Preserve old data:**
   - Manually rename old CSV files
   - Create archive folder for backups

3. **Check for duplicates:**
   ```bash
   # Windows
   Get-ChildItem output/channels_*.csv
   ```

## Data Export Issues

### "No subscriptions found"

**Error Message:**
```
Warning: No subscriptions found for account [email]
```

**Causes:**
- Account has no subscriptions
- Permissions too restricted
- Private subscriptions

**Solutions:**

1. **Verify account:**
   - Log into YouTube with that account
   - Check Subscriptions page manually

2. **Grant permissions:**
   - Delete token file: `secret/token_[email].pickle`
   - Run script again
   - Grant full permissions when prompted

3. **Check subscription privacy:**
   - YouTube settings → Privacy → Subscriptions
   - Ensure subscriptions are not hidden

### "CSV file is empty"

**Error Message:**
```
channels_[email].csv (0 bytes)
```

**Causes:**
- Export failed silently
- No data retrieved
- Permission issue

**Solutions:**

1. **Check for errors in console:**
   - Look for error messages before completion
   - Note any warnings

2. **Try manual export:**
   - Log into YouTube manually
   - Try accessing subscriptions page
   - Test YouTube is working

3. **Re-run with fresh token:**
   ```bash
   # Windows
   Remove-Item "secret/token_[email].pickle"
   
   # Mac/Linux
   rm secret/token_[email].pickle
   ```
   - Run script again

### "CSV file corrupted"

**Error Message:**
```
Excel shows broken data / CSV cannot open
```

**Causes:**
- Special characters not escaped
- File incomplete
- Wrong encoding

**Solutions:**

1. **Try opening with different tool:**
   - Excel, Google Sheets, or text editor
   - Some tools handle encoding better

2. **Check for special characters:**
   - Some channel names have unicode characters
   - Ensure file encoding is UTF-8

3. **Regenerate file:**
   - Delete corrupted CSV
   - Delete corresponding token file
   - Run script again

## Network and Connection Issues

### "Network timeout"

**Error Message:**
```
Error: Connection timeout. Please check your internet connection.
```

**Causes:**
- Internet connection unstable
- Google servers temporarily down
- Network firewall blocking requests
- VPN issues

**Solutions:**

1. **Check internet connection:**
   ```bash
   # Windows
   ping google.com
   ```

2. **Try again:**
   - Wait a few seconds
   - Run script again

3. **Check firewall:**
   - Windows Firewall may block connections
   - Add Python to firewall exceptions
   - Or temporarily disable firewall for testing

4. **Disable VPN:**
   - If using VPN, try disabling it
   - Some VPNs block Google APIs

5. **Check proxy settings:**
   - Ensure no proxy is interfering
   - Configure Python to use correct proxy if needed

### "SSL Certificate Error"

**Error Message:**
```
Error: SSL: CERTIFICATE_VERIFY_FAILED
```

**Causes:**
- Antivirus intercepting HTTPS
- Incorrect system certificates
- System clock wrong

**Solutions:**

1. **Update certificates:**
   ```bash
   # Windows - open Python certificate installer
   /Applications/Python*/Install\ Certificates.command
   ```

2. **Check system time:**
   - Sync system clock
   - Wrong time breaks SSL verification

3. **Check antivirus:**
   - Some antivirus software intercepts HTTPS
   - Try temporarily disabling antivirus
   - Add Python to antivirus whitelist

4. **Update Python:**
   ```bash
   python -m pip install --upgrade certifi
   ```

## Performance Issues

### "Script running very slowly"

**Causes:**
- Large subscription count
- Slow internet connection
- System resource constraints

**Solutions:**

1. **This is normal:**
   - Large subscription lists take time
   - Average: 2-5 seconds per account

2. **Close other programs:**
   - Free up system resources
   - Close browser tabs, large applications

3. **Check internet speed:**
   ```bash
   # Test connection
   ping -n 5 8.8.8.8
   ```

4. **Reduce account count:**
   - Process fewer accounts at once
   - Can be split across multiple runs

### "High memory usage"

**Causes:**
- Large subscription lists
- Memory leak (rare)

**Solutions:**

1. **This is expected:**
   - Large lists require more memory
   - Python holds data in memory during processing

2. **Restart script:**
   - Run again to reset memory

3. **Check for other programs:**
   - Close unnecessary applications
   - Check Task Manager for resource hogs

## Advanced Troubleshooting

### Enable Debug Logging

**Add to see detailed logs:**

Edit the Python file and add before import statements:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

This will show detailed API calls and debugging information.

### Check Python Installation

```bash
# Verify Python version
python --version

# Should be 3.7 or higher
# If not, install newer version from python.org
```

### Verify Dependencies

```bash
# List installed packages
pip list

# Should show:
# - google-api-python-client
# - google-auth-oauthlib
# - google-auth-httplib2

# Reinstall if missing
pip install -r requirements.txt
```

### Clear Cache and Tokens

**Complete reset (if all else fails):**

```bash
# Delete all tokens
# Windows
Remove-Item "secret/token_*.pickle"

# Mac/Linux
rm secret/token_*.pickle

# Delete Python cache
# Windows
Remove-Item "__pycache__" -Recurse

# Mac/Linux
rm -rf __pycache__
find . -type d -name __pycache__ -exec rm -r {} +
```

Then run the script again.

### Check Google Cloud Console

Verify your Google Cloud setup:

1. Go to console.cloud.google.com
2. Select correct project (check dropdown)
3. Check APIs & Services:
   - YouTube Data API v3 should be "Enabled"
   - Quota should show usage

4. Check Credentials:
   - OAuth client should exist
   - Credentials JSON downloadable

5. Check OAuth Screen:
   - All required fields filled
   - All test user emails added

### View Error Logs

**From console output:**
- Read error messages carefully
- Note exact error text
- Include in issue reports

**From file (if configured):**
```bash
# Check for log files
# Windows
Get-ChildItem *.log

# Mac/Linux
ls -la *.log
```

### Contact Support

If still stuck:

1. **Review this guide:**
   - Check each section carefully

2. **Check documentation:**
   - README.md
   - SECURITY.md

3. **Search GitHub Issues:**
   - Similar issue might already be solved
   - https://github.com/abanmitra/youtube-subscription-extractor/issues

4. **Create new issue:**
   - Include error message
   - Include steps to reproduce
   - Include Python version and OS
   - Include output of: `pip list`

5. **Email support:**
   - abanmitra@gmail.com
   - Include all information above

---

## Quick Reference

| Issue | Quick Fix |
|-------|-----------|
| Credentials not found | Put `credentials_config.json` in `secret/` folder |
| Access denied | Add email to Test Users in Google Cloud Console |
| Token expired | Delete `secret/token_[email].pickle` |
| API not enabled | Enable YouTube Data API v3 in Google Cloud Console |
| No subscriptions | Check YouTube account has subscriptions and they're public |
| Network timeout | Check internet connection, try again |
| Script slow | This is normal for large subscription counts |

---

**Still need help?** See [README.md](README.md) or email abanmitra@gmail.com

**Last Updated**: November 2025
