"""
YouTube API module for fetching subscription data.

This module handles interactions with the YouTube Data API v3 to read
subscriptions from YouTube accounts.
"""

from typing import List, Dict, Any, Optional


def get_channel_category(channel_id: str, youtube: Any) -> str:
    """
    Fetch channel category/topic using channel details API.
    
    Args:
        channel_id (str): The YouTube channel ID.
        youtube (Resource): Authenticated YouTube API service object.
    
    Returns:
        str: Comma-separated list of categories, or 'General'/'Unknown' if not available.
    """
    try:
        request = youtube.channels().list(
            part='topicDetails,snippet',
            id=channel_id
        )
        response = request.execute()
        
        if response['items']:
            item = response['items'][0]
            # Get topic categories if available
            if 'topicDetails' in item and 'topicDetails' in item.get('topicDetails', {}):
                categories = [
                    cat.split('/')[-1].replace('_', ' ')
                    for cat in item['topicDetails'].get('topicCategories', [])
                ]
                return ', '.join(categories[:3]) if categories else 'General'
            return 'General'
        return 'Unknown'
    except Exception as e:
        print(f"Warning: Error fetching category for {channel_id}: {str(e)}")
        return 'Unknown'


def fetch_subscriptions(
    youtube: Any,
    account_name: str,
) -> tuple[List[str], Dict[str, List[Dict[str, Any]]]]:  
    """
    Fetch all subscriptions from a YouTube account.
    
    Args:
        youtube (Resource): Authenticated YouTube API service object.
        account_name (str): The account name/email for tracking.
    
    Returns:
        tuple: (subscriptions list, account_channels dict)
            - subscriptions: List of channel titles
            - account_channels: Dict mapping account to their channels
    
    Raises:
        Exception: If API call fails with permission or other errors.
    """
    subscriptions = []
    account_channels_list = []
    next_page_token = None
    
    print(f"Fetching subscriptions for account: {account_name}")
    
    try:
        while True:
            request = youtube.subscriptions().list(
                part='snippet',
                mine=True,
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()
            
            for item in response.get('items', []):
                channel_id = item['snippet']['resourceId']['channelId']
                channel_title = item['snippet']['title']
                
                # Get channel category
                category = get_channel_category(channel_id, youtube)
                
                # Add to account's subscription list
                account_channels_list.append({
                    'channel_id': channel_id,
                    'name': channel_title,
                    'category': category,
                    'type': 'Channel',
                    'link': f'https://www.youtube.com/channel/{channel_id}',
                    'is_new_to_merged_list': 'Yes'
                })
                
                subscriptions.append(channel_title)
            
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
        
        print(f"  Found {len(subscriptions)} subscriptions")
        return subscriptions, {account_name: account_channels_list}
        
    except Exception as e:
        error_msg = str(e)
        print(f"\n⚠️  Error fetching subscriptions for {account_name}:")
        print(f"   Error details: {error_msg}")
        
        # Check for common permission issues
        if "forbidden" in error_msg.lower() or "403" in error_msg:
            print(f"\n   💡 SOLUTION: Permission denied")
            print(f"   🔧 Try these steps:")
            print(f"   1. Delete token_{account_name}.pickle file from secret/ folder")
            print(f"   2. Make sure '{account_name}' is added as a Test User:")
            print(f"      - Go to Google Cloud Console → OAuth consent screen")
            print(f"      - Add Test Users section → Add Users → {account_name}")
            print(f"   3. Ensure YouTube Data API v3 is enabled")
            print(f"   4. Re-run the script to re-authenticate with proper permissions\n")
        elif "invalid_grant" in error_msg.lower():
            print(f"\n   💡 SOLUTION: Invalid credentials - Token may have expired")
            print(f"   🔧 Delete token_{account_name}.pickle and run again\n")
        elif "notfound" in error_msg.lower() or "404" in error_msg:
            print(f"\n   💡 NOTE: No subscriptions found (or subscriptions list is empty)\n")
        
        return [], {account_name: []}
