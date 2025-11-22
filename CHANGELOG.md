# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned Features
- [ ] GUI interface for easier operation
- [ ] Direct merge and analysis tools
- [ ] Support for playlists export
- [ ] Advanced filtering and sorting
- [ ] Database storage option
- [ ] Web dashboard for account management

## [1.0.0] - 2025-11-22

### Added

#### Core Features
- Multi-account YouTube subscription extraction
- OAuth 2.0 secure authentication
- Individual per-account CSV export
- Channel information capture (ID, name, category, link)
- Automatic token management and refresh

#### Utilities
- `youtube_merger.py`: Merge multiple account subscriptions into single CSV
- Duplicate detection across accounts
- CSV comparison tools

#### Documentation
- Comprehensive README with step-by-step setup
- Security best practices guide (SECURITY.md)
- Troubleshooting guide for common issues
- Detailed error messages and solutions

#### Developer Features
- Type hints throughout codebase
- Detailed docstrings for all functions
- Modular architecture with separate concerns
- Clean error handling and logging

### Features

#### Authentication (`auth.py`)
- OAuth 2.0 implementation using google-auth-oauthlib
- Secure token storage and management
- Automatic token refresh mechanism
- Support for multiple concurrent authentications
- Credentials configuration management

#### Data Fetching (`youtube_api.py`)
- YouTube Data API v3 integration
- Subscription list retrieval
- Channel metadata extraction
- Batch request handling
- Error recovery and retries

#### Data Export (`csv_handler.py`)
- Read account email lists from CSV
- Export subscriptions to organized CSV files
- Channel data formatting
- File naming conventions
- Batch export operations

#### Merging (`youtube_merger.py`)
- Combine multiple account CSVs
- Duplicate detection
- Common subscriptions identification
- Summary statistics

### Security
- Read-only YouTube API permissions
- No password storage or transmission
- Encrypted token files
- `.gitignore` configuration
- Credentials separation in `secret/` folder

### Testing & Quality
- Manual test procedure documentation
- Multi-account test support
- Error scenario coverage

## Version History

### Version 0.9.0 (Beta)
- Initial beta release
- Core functionality complete
- Security measures in place
- Community feedback gathering phase

---

## Guidelines for Updates

### Version Numbering

- **MAJOR**: Breaking changes, significant restructuring
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, minor improvements

### When to Update

- Release tags after milestones
- Document all changes in this file
- Update version in setup/config files
- Create GitHub releases with notes

### Categories for Changes

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Previously deprecated features
- **Fixed**: Bug fixes
- **Security**: Security improvements

---

## Future Roadmap

### Phase 2 - Enhanced Features
- GUI Application
- Advanced analytics
- Playlist support
- Custom filtering

### Phase 3 - Integration
- Database support
- Cloud synchronization
- API endpoints
- Mobile apps

### Phase 4 - Scale
- Performance optimization
- Distributed processing
- Enterprise features
- White-label solution

---

## Support

For issues or questions about a specific version:
1. Check the version notes above
2. Review the README.md
3. Check TROUBLESHOOTING.md
4. Open an issue on GitHub

---

**Last Updated**: November 2025

[Unreleased]: https://github.com/abanmitra/youtube-subscription-extractor/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/abanmitra/youtube-subscription-extractor/releases/tag/v1.0.0
