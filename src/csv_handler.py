"""
CSV handler module for YouTube subscription data.

This module handles reading input CSV files with account emails and exporting
subscription data to CSV format.
"""

import csv
import os
from typing import List, Dict, Any


def read_accounts_csv(csv_file: str) -> List[Dict[str, str]]:
    """
    Read YouTube accounts (email IDs) from a CSV file.
    
    Handles files with or without headers. Common headers like 'username',
    'email', 'mail id', 'email id', 'account' are detected and ignored.
    If no recognized header is found, treats first line as an email ID.
    
    Args:
        csv_file (str): Path to the CSV file containing email IDs.
    
    Returns:
        List[Dict[str, str]]: List of account dictionaries with 'username' key.
    
    Raises:
        FileNotFoundError: If the CSV file doesn't exist.
    """
    if not os.path.exists(csv_file):
        raise FileNotFoundError(
            f"❌ ERROR: CSV file '{csv_file}' not found!\n"
            "Please create the file with account information."
        )
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        
        if not lines:
            return []
        
        # Common header patterns to detect and ignore
        header_patterns = {'username', 'email', 'mail id', 'email id', 'account', 'mail', 'id'}
        first_line_lower = lines[0].lower().strip()
        
        # Check if first line is a header
        is_header = any(pattern in first_line_lower for pattern in header_patterns)
        
        # Start from line 1 if header detected, otherwise from line 0
        start_idx = 1 if is_header else 0
        
        # Convert email lines to account dictionaries
        accounts = [{'username': email} for email in lines[start_idx:]]
        
        if is_header:
            print(f"✓ Detected and skipped header: '{lines[0]}'")
        
        return accounts
    except Exception as e:
        raise Exception(f"Error reading CSV file '{csv_file}': {str(e)}")




def export_account_files(
    account_channels: Dict[str, List[Dict[str, Any]]],
    output_dir: str = 'output'
) -> None:
    """
    Export separate CSV files for each account with their subscribed channels.
    
    Args:
        account_channels (Dict): Dictionary mapping account name to their channels.
        output_dir (str): Directory to store output files.
    
    Raises:
        Exception: If export fails.
    """
    if not account_channels:
        print("⚠️  No account channels to export!")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print("\nExporting individual account subscription files...")
    
    try:
        for account_name, channels in account_channels.items():
            if not channels:
                print(f"  ⊘ Skipped {account_name} (no channels)")
                continue
            
            # Create filename from account email (remove domain for cleaner names)
            safe_name = account_name.split('@')[0] if '@' in account_name else account_name
            output_file = os.path.join(output_dir, f"channels_{safe_name}.csv")
            
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                fieldnames = [
                    'Channel ID',
                    'Channel Name',
                    'Category',
                    'Type',
                    'Channel Link',
                    'New to List'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()
                for channel_data in sorted(
                    channels,
                    key=lambda x: x['name'].lower()
                ):
                    writer.writerow({
                        'Channel ID': channel_data['channel_id'],
                        'Channel Name': channel_data['name'],
                        'Category': channel_data['category'],
                        'Type': channel_data['type'],
                        'Channel Link': channel_data['link'],
                        'New to List': channel_data['is_new_to_merged_list']
                    })
            
            print(f"  ✓ Exported {len(channels)} channels to: {output_file}")
    except Exception as e:
        raise Exception(f"Error exporting account files: {str(e)}")
