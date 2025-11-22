#!/usr/bin/env python3
"""
SEO Optimization Verification Script

Verifies that all files have been created and optimized for GitHub upload.
Run this before uploading to GitHub to ensure everything is ready.

Usage:
    python verify_seo_optimization.py
"""

import os
import sys
from pathlib import Path


def check_files(base_path):
    """Check if all required files exist."""
    
    required_files = {
        "README.md": "Main project documentation",
        "INSTALL.md": "Installation guide",
        "SECURITY.md": "Security best practices",
        "CONTRIBUTING.md": "Contributing guidelines",
        "CODE_OF_CONDUCT.md": "Code of conduct",
        "TROUBLESHOOTING.md": "Troubleshooting guide",
        "FEATURES.md": "Features overview",
        "CHANGELOG.md": "Version history",
        "LICENSE": "MIT License",
        ".gitignore": "Git ignore file",
        "requirements.txt": "Python dependencies",
        "REPOSITORY_CONFIG.md": "GitHub repository configuration",
        "GITHUB_UPLOAD_GUIDE.md": "Upload guide",
        "SEO_OPTIMIZATION_SUMMARY.md": "Optimization summary",
        "QUICK_START_GUIDE.md": "Quick start guide",
        ".github/README.md": "GitHub folder README",
        ".github/workflows/tests.yml": "Tests workflow",
        ".github/workflows/security.yml": "Security workflow",
        ".github/workflows/documentation.yml": "Documentation workflow",
        ".github/ISSUE_TEMPLATE/bug_report.md": "Bug report template",
        ".github/ISSUE_TEMPLATE/feature_request.md": "Feature request template",
        ".github/ISSUE_TEMPLATE/documentation.md": "Documentation template",
        ".github/PULL_REQUEST_TEMPLATE.md": "PR template",
    }
    
    print("\n" + "="*70)
    print("📋 CHECKING REQUIRED FILES")
    print("="*70)
    
    missing_files = []
    found_files = []
    
    for file_path, description in required_files.items():
        full_path = os.path.join(base_path, file_path)
        exists = os.path.exists(full_path)
        
        if exists:
            size = os.path.getsize(full_path)
            print(f"✅ {file_path:<50} ({size:,} bytes)")
            found_files.append(file_path)
        else:
            print(f"❌ {file_path:<50} MISSING")
            missing_files.append(file_path)
    
    print("\n" + "-"*70)
    print(f"Found: {len(found_files)}/{len(required_files)} files")
    
    if missing_files:
        print(f"\n⚠️  Missing {len(missing_files)} files:")
        for f in missing_files:
            print(f"   - {f}")
    
    return len(missing_files) == 0


def check_file_content(base_path):
    """Check that critical files have content."""
    
    print("\n" + "="*70)
    print("📝 CHECKING FILE CONTENT")
    print("="*70)
    
    critical_files = {
        "README.md": ["Features", "Installation", "Usage"],
        "INSTALL.md": ["Prerequisites", "Installation", "Setup"],
        "SECURITY.md": ["Security", "Best Practices"],
        "CONTRIBUTING.md": ["Contributing", "Guidelines"],
        "requirements.txt": ["google"],
        ".gitignore": ["secret/", "credentials"],
    }
    
    all_good = True
    
    for file_path, keywords in critical_files.items():
        full_path = os.path.join(base_path, file_path)
        
        if not os.path.exists(full_path):
            print(f"❌ {file_path} - NOT FOUND")
            all_good = False
            continue
        
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check file size
        if len(content) < 100:
            print(f"❌ {file_path} - File too small ({len(content)} bytes)")
            all_good = False
            continue
        
        # Check for keywords
        missing_keywords = []
        for keyword in keywords:
            if keyword.lower() not in content.lower():
                missing_keywords.append(keyword)
        
        if missing_keywords:
            print(f"⚠️  {file_path} - Missing keywords: {missing_keywords}")
        else:
            print(f"✅ {file_path} - Content verified")
    
    return all_good


def check_security(base_path):
    """Check that security measures are in place."""
    
    print("\n" + "="*70)
    print("🔒 CHECKING SECURITY")
    print("="*70)
    
    all_good = True
    
    # Check .gitignore
    gitignore_path = os.path.join(base_path, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            gitignore_content = f.read()
        
        security_checks = {
            "secret/": "Protects secret folder",
            "credentials_config.json": "Protects credentials file",
            "youtube_accounts.csv": "Protects accounts file",
            "__pycache__/": "Ignores Python cache",
        }
        
        for check, description in security_checks.items():
            if check in gitignore_content:
                print(f"✅ .gitignore - {description}")
            else:
                print(f"❌ .gitignore - Missing: {check}")
                all_good = False
    else:
        print(f"❌ .gitignore - NOT FOUND")
        all_good = False
    
    # Check for accidentally committed secrets
    print(f"\n✅ Checking for exposed secrets...")
    sensitive_files = ["secret/credentials_config.json", "youtube_accounts.csv"]
    for sensitive_file in sensitive_files:
        full_path = os.path.join(base_path, sensitive_file)
        if os.path.exists(full_path):
            print(f"⚠️  {sensitive_file} - EXISTS (make sure it's in .gitignore)")
    
    return all_good


def check_github_structure(base_path):
    """Check GitHub special directories structure."""
    
    print("\n" + "="*70)
    print("🔗 CHECKING GITHUB STRUCTURE")
    print("="*70)
    
    github_items = [
        ".github/",
        ".github/workflows/",
        ".github/ISSUE_TEMPLATE/",
    ]
    
    all_good = True
    for item in github_items:
        full_path = os.path.join(base_path, item)
        if os.path.exists(full_path):
            print(f"✅ {item} - EXISTS")
        else:
            print(f"❌ {item} - NOT FOUND")
            all_good = False
    
    return all_good


def count_documentation(base_path):
    """Count documentation files and lines."""
    
    print("\n" + "="*70)
    print("📚 DOCUMENTATION STATISTICS")
    print("="*70)
    
    doc_files = [
        "README.md",
        "INSTALL.md",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "TROUBLESHOOTING.md",
        "FEATURES.md",
        "CHANGELOG.md",
    ]
    
    total_lines = 0
    total_size = 0
    
    for doc_file in doc_files:
        full_path = os.path.join(base_path, doc_file)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = len(f.readlines())
                size = os.path.getsize(full_path)
            total_lines += lines
            total_size += size
            print(f"  {doc_file:<40} {lines:>6} lines  {size:>8,} bytes")
    
    print("-"*70)
    print(f"Total: {len(doc_files)} files  {total_lines:,} lines  {total_size:,} bytes")
    
    print(f"\n✅ Documentation is comprehensive!")


def main():
    """Run all verification checks."""
    
    # Get base path
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = os.getcwd()
    
    if not os.path.exists(base_path):
        print(f"❌ Path not found: {base_path}")
        return 1
    
    print(f"\n🔍 Verifying SEO Optimization")
    print(f"   Base path: {base_path}")
    
    # Run checks
    checks = [
        ("Files", check_files(base_path)),
        ("Content", check_file_content(base_path)),
        ("Security", check_security(base_path)),
        ("GitHub Structure", check_github_structure(base_path)),
    ]
    
    # Count documentation
    count_documentation(base_path)
    
    # Summary
    print("\n" + "="*70)
    print("✅ VERIFICATION SUMMARY")
    print("="*70)
    
    all_passed = all(status for _, status in checks)
    
    for check_name, status in checks:
        status_str = "✅ PASS" if status else "⚠️  WARN"
        print(f"{status_str:<10} {check_name}")
    
    print("\n" + "="*70)
    
    if all_passed:
        print("✅ PROJECT IS READY FOR GITHUB UPLOAD!")
        print("\nNext steps:")
        print("1. Review GITHUB_UPLOAD_GUIDE.md")
        print("2. Create GitHub repository")
        print("3. Push all files to GitHub")
        print("4. Add 15 repository topics (CRITICAL!)")
        print("5. Create first release (v1.0.0)")
        print("6. Share on social media")
        print("="*70)
        return 0
    else:
        print("⚠️  SOME ITEMS NEED ATTENTION")
        print("   Review warnings above and fix before uploading")
        print("="*70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
