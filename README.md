# YouTube Subscription Extractor

**Extract, backup, and analyze your YouTube subscriptions from multiple accounts with one click.**

A powerful Python application to read YouTube subscription lists from multiple accounts and extract them into individual CSV files with comprehensive channel information, secure OAuth 2.0 authentication, and advanced data merge capabilities.

## 🎯 Overview

This tool allows you to **extract subscription lists from multiple YouTube accounts** and save them as individual CSV files. Each file contains the complete list of subscribed channels for that account, making it easy to **analyze, backup, migrate, compare, and organize your subscriptions** across multiple YouTube channels. Perfect for content creators, researchers, and YouTube enthusiasts who manage multiple accounts.

**Core Keywords**: YouTube subscriptions extractor | Python subscription backup | multi-account YouTube export | OAuth authentication YouTube | CSV channel export | YouTube data analysis | subscription archiver | channel data mining | YouTube API Python | batch subscription extraction

## ✨ Key Features

- **🎯 Multi-Account YouTube Support**: Extract subscriptions from unlimited YouTube accounts simultaneously
- **📊 Complete Subscription Extraction**: Reads your entire subscribed channels list from each account with full metadata
- **📋 Rich Channel Data**: Captures channel IDs, names, categories, content types, links, and subscription status
- **💾 CSV Exports**: Generates per-account CSV files for backup, analysis, migration, and archival
- **🔒 OAuth 2.0 Security**: Industry-standard authentication - passwords never stored, read-only API access
- **🔄 Smart Subscription Merging**: Combine multiple account subscriptions to identify common interests and trends
- **⚡ Automatic Token Lifecycle**: Transparent token creation, refresh, and management
- **🛡️ Enterprise Security**: Encrypted tokens, sensitive data protection, comprehensive security documentation
- **📱 Cross-Platform**: Works seamlessly on Windows, macOS, and Linux with Python 3.7+
- **🏗️ Batch Processing**: Process hundreds of channels per account in seconds

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Web browser (for OAuth authentication)
- Google Account with YouTube access

## Installation

### Step 1: Install Dependencies

Open PowerShell or Command Prompt in the project directory and run:

```powershell
pip install -r requirements.txt
```

### Step 2: Set Up Google Cloud Project

Complete the setup guide below to obtain OAuth credentials from Google Cloud Console.

## Configuration

### Google Cloud Setup (Required)

Before running the application, you must:

1. **Create a Google Cloud Project**
   - Go to https://console.cloud.google.com/
   - Create a new project

2. **Enable YouTube Data API v3**
   - Navigate to APIs & Services → Library
   - Search for "YouTube Data API v3"
   - Click Enable

3. **Create OAuth Credentials**
   - Go to APIs & Services → Credentials
   - Click "Create Credentials" → "OAuth client ID"
   - Select "Desktop application"
   - Download the credentials JSON file
   - Rename to `credentials_config.json` and place in the `secret/` folder

4. **Configure OAuth Consent Screen**
   - Go to OAuth consent screen
   - Add the email addresses of all YouTube accounts you'll use as test users

For detailed step-by-step instructions, see the SECURITY.md file.

### Prepare YouTube Accounts File

Create or update `youtube_accounts.csv` with your YouTube account emails:

```csv
username
user1@gmail.com
user2@gmail.com
user3@gmail.com
```

**Note**: The file must have a `username` header followed by email addresses, one per line.

## Usage

### Running the Application

Execute the script using the provided launcher:

**Windows:**
```powershell
.\run.bat
```

**macOS/Linux:**
```bash
./run.sh
```

Or run directly with Python:

```powershell
python src\youtube_extractor.py
```

### During Execution

For each account, a browser window will automatically open:

1. Sign in with your Google account
2. Grant permission when prompted
3. Close the browser tab when done

The script will continue automatically.

### Output

After completion, you'll find:

- **`output/channels_[username].csv`** - Individual files per account showing their subscriptions

Each file contains the complete subscription list for that account.

Example output structure:

```
Channel ID,Channel Name,Category,Type,Channel Link,New to List
UCxxxx,Tech News Daily,Technology,Channel,https://www.youtube.com/channel/UCxxxx,Yes
UCyyyy,Python Programming,Education,Channel,https://www.youtube.com/channel/UCyyyy,Yes
UCzzzz,Music Beats,Music,Channel,https://www.youtube.com/channel/UCzzzz,Yes
```

## Project Structure

```
youtube/
├── src/
│   ├── youtube_extractor.py    Main application entry point
│   ├── auth.py                 OAuth 2.0 authentication
│   ├── youtube_api.py          YouTube API interactions
│   └── csv_handler.py          CSV operations
├── youtube_accounts.csv        Your account emails (user input)
├── requirements.txt            Python dependencies
├── README.md                   This file
├── SECURITY.md                 Security best practices
├── run.bat                     Windows launcher
├── run.sh                      Unix launcher
├── secret/                     Credentials and tokens (keep private)
└── output/                     Generated subscription CSV files
```

## Sample Files

### Input: youtube_accounts.csv

```csv
username
john@gmail.com
jane@gmail.com
```

This file contains the email addresses of YouTube accounts to process. You can use any filename and provide the full path when running the application.

### Output: channels_john.csv

```csv
Channel ID,Channel Name,Category,Type,Channel Link,New to List
UCxxxxxx,Tech Channel,Technology,Channel,https://www.youtube.com/channel/UCxxxxx,Yes
UCyyyyyy,Music Channel,Music,Channel,https://www.youtube.com/channel/UCyyyyy,Yes
```

## Troubleshooting

### "Credentials config file not found"

**Solution**: Ensure `credentials_config.json` is in the `secret/` folder at `secret/credentials_config.json`

### "OAuth Access Denied"

**Solution**: 
1. Add all email addresses to Test Users in Google Cloud Console
2. Delete token files from `secret/` folder
3. Run the script again

### "Permission denied when reading subscriptions"

**Solution**:
1. Verify the account email is added as a Test User in Google Cloud Console
2. Check that YouTube Data API v3 is enabled
3. Delete the corresponding `token_[email].pickle` file from the `secret/` folder
4. Run the script again to re-authenticate with fresh permissions

### "YouTube Data API is not enabled"

**Solution**: 
1. Go to Google Cloud Console → APIs & Services → Library
2. Search for and enable "YouTube Data API v3"
3. Wait a few minutes for activation
4. Try again

### Token Expired

**Solution**: Delete the corresponding `token_[email].pickle` file from the `secret/` folder and run again

## Security

For detailed security information and best practices:

- See `SECURITY.md` for comprehensive security guidelines
- Never share the `secret/` folder contents
- Never commit the `secret/` folder to version control
- Keep `youtube_accounts.csv` confidential

## Support

For issues or questions:

1. Check the SECURITY.md file for security-related questions
2. Review error messages in the console output
3. Verify all credentials and files are in the correct locations
4. Ensure your Google account permissions are properly configured

## Documentation

- **[README.md](README.md)** - Getting started guide and basic usage
- **[SECURITY.md](SECURITY.md)** - Security best practices and data protection
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Development guidelines and how to contribute
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** - Community standards and conduct
- **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues and solutions
- **[CHANGELOG.md](CHANGELOG.md)** - Version history and updates
- **[FEATURES.md](FEATURES.md)** - Comprehensive feature documentation

## 💼 Use Cases & Applications

This **YouTube subscription backup and analysis tool** is perfect for:

- **Content Creators & YouTubers**: Instantly back up all subscriptions from multiple YouTube channels, create comprehensive channel archives, migrate subscriptions between accounts
- **Research & Analytics**: Analyze channel categories, content preferences, subscription patterns, identify trending topics across multiple accounts
- **Bulk Account Management**: Track and compare recommendations across multiple accounts, manage team YouTube channels, organize subscriptions at scale
- **Data Science & Analytics**: Export subscription data for advanced visualization, statistical analysis, machine learning, trend identification
- **Channel Migration & Consolidation**: Transfer subscriptions when migrating to new accounts, consolidate multiple channels, dedup subscriptions
- **Compliance & Archival**: Archive subscription data for record-keeping, compliance requirements, historical analysis, audit trails
- **Workflow Automation**: Integrate with other tools via CSV, connect to data pipelines, automate reporting, batch operations
- **Market Research**: Analyze competitor channels, track industry subscriptions, discover trending content channels, competitive analysis

## Related Projects & Integration

- Works with Google Sheets for subscription analysis
- Compatible with Excel for data manipulation
- Can be integrated with workflow automation tools
- API-ready for custom integrations
- Supports batch processing for large operations

## Statistics

- **Language**: Python 3.7+
- **License**: MIT
- **API**: YouTube Data API v3
- **Authentication**: OAuth 2.0
- **Data Format**: CSV (universal compatibility)
- **Tested Accounts**: 1-100+ subscriptions per account
- **Typical Speed**: 2-5 seconds per account

## Frequently Asked Questions

**Q: Can I use this on my production YouTube channel?**
A: Yes! This tool uses read-only permissions and never modifies your subscriptions.

**Q: Is my password stored?**
A: No. The application never stores passwords. It uses OAuth 2.0 which is industry standard.

**Q: Can I run this on multiple machines?**
A: Yes, but keep credentials in sync. Use separate OAuth clients for better security.

**Q: What if YouTube changes their API?**
A: We actively maintain compatibility. Updates are documented in CHANGELOG.md

**Q: Can I contribute improvements?**
A: Absolutely! See CONTRIBUTING.md for guidelines.

## Community

- **Report Issues**: [GitHub Issues](https://github.com/abanmitra/youtube-subscription-extractor/issues)
- **Discussions**: [GitHub Discussions](https://github.com/abanmitra/youtube-subscription-extractor/discussions)
- **Email**: abanmitra@gmail.com
- **Security Issues**: Email abanmitra@gmail.com (do not open public issues)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Open Source & Commercial Use

**Personal & Open Source Use**: This project is open source and freely available for personal, educational, and non-commercial purposes.

**Commercial Use & Distribution**: For commercial purposes and distribution of this software, you must contact:

📧 **abanmitra@gmail.com**

---

**Last Updated**: November 2025

**Repository**: [GitHub - YouTube Subscription Extractor](https://github.com/abanmitra/youtube-subscription-extractor)
