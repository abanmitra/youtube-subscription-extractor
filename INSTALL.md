# YouTube Subscription Extractor - Installation Guide

Complete step-by-step installation and setup instructions for the **YouTube subscription backup and extraction tool**. This guide covers everything needed to get the application running on Windows, macOS, and Linux.

**Keywords**: YouTube subscription extractor installation | Python YouTube API setup | OAuth configuration | Google Cloud Console guide | multi-account YouTube setup

## Quick Start (5 minutes)

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Web browser for authentication
- Google Account with YouTube access

### Installation Steps

1. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Google Cloud Credentials** (see [Google Cloud Setup](#google-cloud-setup) below)

3. **Create Accounts File**
   ```csv
   username
   your-email@gmail.com
   ```
   Save as `youtube_accounts.csv`

4. **Run the Application**
   ```bash
   # Windows
   .\run.bat
   
   # macOS/Linux
   ./run.sh
   ```

That's it! Your subscriptions will be exported to `output/` folder.

---

## Detailed Installation

### Step 1: Install Python

#### Windows

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer
3. ✅ **IMPORTANT**: Check "Add Python to PATH"
4. Complete installation
5. Verify installation:
   ```bash
   python --version
   ```

#### macOS

```bash
# Using Homebrew
brew install python3

# Or download from python.org
# https://www.python.org/downloads/macos/
```

Verify:
```bash
python3 --version
```

#### Linux (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

Verify:
```bash
python3 --version
```

### Step 2: Install Dependencies

Navigate to project directory:

```bash
# Windows
cd C:\path\to\youtube-subscription-extractor

# macOS/Linux
cd ~/path/to/youtube-subscription-extractor
```

Install required packages:

```bash
pip install -r requirements.txt
```

**Verify installation:**

```bash
pip list
```

Should show:
- google-api-python-client
- google-auth-oauthlib
- google-auth-httplib2

### Step 3: Google Cloud Setup

#### 3.1 Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click on project dropdown at top
3. Click "NEW PROJECT"
4. Enter project name: `YouTube Subscription Extractor`
5. Click "CREATE"
6. Wait for project creation (1-2 minutes)

#### 3.2 Enable YouTube Data API v3

1. In Google Cloud Console, go to **APIs & Services** → **Library**
2. Search for: `YouTube Data API v3`
3. Click on the API
4. Click "ENABLE"
5. Wait for activation (may take 5-10 minutes)

#### 3.3 Configure OAuth Consent Screen

1. Go to **APIs & Services** → **OAuth consent screen**
2. Select **External** user type
3. Click "CREATE"
4. Fill in required fields:
   - **App name**: YouTube Subscription Extractor
   - **User support email**: your-email@gmail.com
   - **Developer contact**: your-email@gmail.com
5. Click "SAVE AND CONTINUE"
6. On "Scopes" page: Click "SAVE AND CONTINUE"
7. On "Test users" page: Click "ADD USERS"
   - Add all email addresses you'll use
   - Click "ADD"
8. Click "SAVE AND CONTINUE"
9. Review and click "BACK TO DASHBOARD"

#### 3.4 Create OAuth Credentials

1. Go to **APIs & Services** → **Credentials**
2. Click "+ CREATE CREDENTIALS" → "OAuth client ID"
3. If prompted to create OAuth consent screen first, go back and complete 3.3
4. Select **Desktop application** as application type
5. Enter name: `YouTube Subscription Extractor Desktop`
6. Click "CREATE"
7. Click "DOWNLOAD" (JSON file)
8. Save the JSON file

#### 3.5 Place Credentials in Project

1. Create `secret` folder in project root if it doesn't exist:
   ```bash
   mkdir secret
   ```

2. Move downloaded JSON file to `secret/` folder

3. Rename to `credentials_config.json`:
   - Old name: `client_secret_*.json`
   - New name: `credentials_config.json`
   - Location: `secret/credentials_config.json`

4. Verify:
   ```bash
   # Windows
   Test-Path "secret/credentials_config.json"
   
   # macOS/Linux
   test -f secret/credentials_config.json && echo "Found"
   ```

### Step 4: Prepare Accounts File

Create `youtube_accounts.csv` in project root:

```csv
username
your-email@gmail.com
second-account@gmail.com
third-account@gmail.com
```

**Important:**
- First line must be: `username` (header)
- One email per line
- Must match Google account emails exactly
- All emails must be added as Test Users in Google Cloud Console

### Step 5: Verify Installation

Run verification script:

```bash
python -c "
import sys
print(f'Python: {sys.version}')

required = ['google', 'google_auth_oauthlib', 'google_auth_httplib2']
for pkg in required:
    try:
        __import__(pkg)
        print(f'✓ {pkg}')
    except ImportError:
        print(f'✗ {pkg} NOT INSTALLED')
"
```

Check file structure:

```bash
# Windows
Test-Path "secret/credentials_config.json"
Test-Path "youtube_accounts.csv"

# macOS/Linux
test -f secret/credentials_config.json && echo "✓ Credentials found"
test -f youtube_accounts.csv && echo "✓ Accounts file found"
```

### Step 6: First Run

Run the application:

```bash
# Windows
.\run.bat

# macOS/Linux
./run.sh
```

**What to expect:**
1. Browser window opens for each account
2. Sign in with Google account
3. Grant permissions when prompted
4. Close browser tab
5. Process repeats for next account
6. Subscriptions exported to `output/` folder

---

## Advanced Installation

### Virtual Environment Setup (Recommended)

Using a virtual environment keeps dependencies isolated:

#### Windows

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Deactivate when done
deactivate
```

#### macOS/Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Deactivate when done
deactivate
```

### Docker Installation

If you have Docker installed:

```bash
# Build image
docker build -t youtube-extractor .

# Run container
docker run -v $(pwd)/secret:/app/secret \
           -v $(pwd)/output:/app/output \
           youtube-extractor
```

### Conda Installation

If using Anaconda:

```bash
# Create conda environment
conda create -n youtube python=3.10

# Activate environment
conda activate youtube

# Install requirements
pip install -r requirements.txt

# Run application
python src/youtube_extractor.py
```

---

## Troubleshooting Installation

### "Python not found"

**Windows:**
- Restart PowerShell after installation
- Verify Python in PATH: `echo $env:Path`
- Reinstall Python and check "Add Python to PATH"

**macOS/Linux:**
- Use `python3` instead of `python`
- Update PATH: `export PATH="/usr/local/bin:$PATH"`

### "pip not found"

```bash
# Windows
python -m pip install -r requirements.txt

# macOS/Linux
python3 -m pip install -r requirements.txt
```

### "Permission denied" errors

```bash
# Add user flag
pip install --user -r requirements.txt

# Or use virtual environment (recommended)
python -m venv venv
```

### "Google API not enabled"

- Go to Google Cloud Console
- Select correct project (check project dropdown)
- Wait 10 minutes after enabling
- Clear browser cache and retry

### "Credentials file not found"

```bash
# Verify file exists
Test-Path "secret/credentials_config.json"

# Check content is valid JSON
python -c "import json; json.load(open('secret/credentials_config.json'))"
```

### "Requirements installation fails"

Try with upgraded pip:

```bash
# Windows
python -m pip install --upgrade pip
pip install -r requirements.txt

# macOS/Linux
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

---

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.7 | 3.10+ |
| RAM | 512 MB | 2 GB |
| Disk | 100 MB | 500 MB |
| Internet | Required | Always-on |
| OS | Windows 7+ / macOS 10.12+ / Ubuntu 16.04+ | Latest LTS |

---

## Post-Installation

### Verify Setup

1. ✅ Python installed
2. ✅ Dependencies installed
3. ✅ Google Cloud project created
4. ✅ YouTube API enabled
5. ✅ OAuth credentials downloaded
6. ✅ Credentials in `secret/` folder
7. ✅ Accounts CSV created
8. ✅ First run successful

### Next Steps

1. Read [README.md](../README.md) for basic usage
2. Review [SECURITY.md](../SECURITY.md) for security practices
3. Check [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) for common issues
4. Explore [FEATURES.md](../FEATURES.md) for available features

### Uninstall

To remove the project:

```bash
# Delete project folder
# Windows
rmdir /s youtube-subscription-extractor

# macOS/Linux
rm -rf youtube-subscription-extractor
```

To remove Python (if not using for other projects):
- Windows: Control Panel → Uninstall a Program
- macOS: `/usr/local/bin/python*` manual deletion or Homebrew `brew uninstall python3`
- Linux: `sudo apt-get remove python3`

---

## Getting Help

- Check [TROUBLESHOOTING.md](../TROUBLESHOOTING.md)
- Review [README.md](../README.md)
- Check [GitHub Issues](https://github.com/abanmitra/youtube-subscription-extractor/issues)
- Email: abanmitra@gmail.com

---

**Last Updated**: November 2025
