"""
YouTube Channel Merger - Main Entry Point

Merges YouTube subscriptions from multiple accounts into a single, deduplicated channel list.

This script coordinates authentication, data fetching, and export operations
by using specialized modules for each functionality area.

Modules:
    - auth: Handles OAuth 2.0 authentication with Google APIs
    - youtube_api: Fetches subscription and channel data from YouTube
    - csv_handler: Reads input and exports data to CSV files
"""

import json
import sys
import os
from typing import Dict, Any, List

from auth import load_credentials_config, authenticate
from youtube_api import fetch_subscriptions
from csv_handler import read_accounts_csv, export_merged_channels, export_account_files


def process_account(
    account: Dict[str, str],
    credentials_config: Dict[str, Any],
    all_channels: Dict[str, Dict[str, Any]],
    account_channels: Dict[str, List[Dict[str, Any]]],
    account_idx: int,
    total_accounts: int,
) -> None:
    """
    Process a single YouTube account.
    
    Authenticates with the account, fetches subscriptions, and updates the
    master channel list and account-specific channel list.
    
    Args:
        account (Dict): Account information with 'username' key.
        credentials_config (Dict): OAuth credentials configuration.
        all_channels (Dict): Master dictionary of all unique channels.
        account_channels (Dict): Dictionary mapping accounts to their channels.
        account_idx (int): Current account index (for display).
        total_accounts (int): Total number of accounts to process.
    """
    username = account.get('username', '').strip()
    if not username:
        return
    
    print(f"\n[{account_idx}/{total_accounts}] Processing account: {username}")
    print("=" * 60)
    
    try:
        # Authenticate with the account
        print(f"Please authenticate with account: {username}")
        youtube = authenticate(username, credentials_config, token_dir='secret')
        
        # Fetch subscriptions and update master lists
        subs, new_channels, new_account_channels = fetch_subscriptions(youtube, username)
        
        # Merge results into master dictionaries
        all_channels.update(new_channels)
        account_channels.update(new_account_channels)
        
    except Exception as e:
        print(f"❌ Failed to process account '{username}': {str(e)}")


def main() -> int:
    """
    Main execution function.
    
    Orchestrates the full workflow:
    1. Load credentials configuration
    2. Read accounts from CSV (file path from command-line argument)
    3. Process each account (authenticate and fetch subscriptions)
    4. Export merged channel list
    5. Export individual account files
    
    Returns:
        int: 0 for success, 1 for failure.
    """
    print("YouTube Channel Merger")
    print("=" * 60)
    
    try:
        # Get file path from command-line argument
        if len(sys.argv) < 2:
            print("❌ Error: No file path provided")
            print("Usage: python youtube_merger.py <file_path>")
            return 1
        
        input_csv = sys.argv[1]
        
        # Get the root directory (parent of src)
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Load credentials configuration
        print("Loading credentials configuration...")
        credentials_config_path = os.path.join(root_dir, 'secret', 'credentials_config.json')
        credentials_config = load_credentials_config(credentials_config_path)
        print("✓ Credentials configuration loaded\n")
        
        # Read accounts from CSV
        print(f"Reading accounts from CSV: {input_csv}")
        accounts = read_accounts_csv(input_csv)
        print(f"✓ Found {len(accounts)} account(s) to process\n")
        
        # Initialize data structures
        all_channels: Dict[str, Dict[str, Any]] = {}
        account_channels: Dict[str, List[Dict[str, Any]]] = {}
        
        # Process each account
        for idx, account in enumerate(accounts, 1):
            process_account(
                account,
                credentials_config,
                all_channels,
                account_channels,
                idx,
                len(accounts)
            )
        
        # Export results
        print(f"\n{'=' * 60}")
        print(f"Total unique channels collected: {len(all_channels)}")
        
        if all_channels:
            output_dir = os.path.join(root_dir, 'output')
            merged_file = os.path.join(output_dir, 'merged_channels.csv')
            export_merged_channels(all_channels, merged_file)
            export_account_files(account_channels, output_dir)
        
        print("\n" + "=" * 60)
        print("✅ Process completed successfully!")
        print("\nOutput files are in the 'output' folder.")
        print("Authentication tokens are stored in the 'secret' folder.")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\n" + "=" * 60)
        print("❌ Process failed!")
        return 1


if __name__ == '__main__':
    exit(main())
