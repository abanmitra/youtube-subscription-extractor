"""
Authentication module for YouTube API.

This module handles OAuth 2.0 authentication with Google's YouTube Data API.
It supports multiple accounts with different OAuth clients.
"""

import os
import json
import pickle
import tempfile
from typing import Optional, Dict, Any

# YouTube API scopes
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']


def load_credentials_config(config_file: str = 'credentials_config.json') -> Dict[str, Any]:
    """
    Load the credentials configuration that maps accounts to OAuth clients.
    
    Args:
        config_file (str): Path to the credentials configuration file.
    
    Returns:
        Dict[str, Any]: The loaded credentials configuration.
    
    Raises:
        FileNotFoundError: If credentials config file doesn't exist.
        ValueError: If the config file has invalid JSON or missing required fields.
    """
    if not os.path.exists(config_file):
        raise FileNotFoundError(
            f"\n❌ ERROR: Credentials config file '{config_file}' not found!\n"
            "Please ensure credentials_config.json exists in the 'secret' folder."
        )
    
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        # Validate structure
        if 'account_to_client_mapping' not in config:
            raise ValueError("Missing 'account_to_client_mapping' in credentials config")
        
        return config
        
    except json.JSONDecodeError:
        raise ValueError(
            f"\n❌ ERROR: '{config_file}' contains invalid JSON.\n"
            "Please ensure the file contains valid configuration."
        )


def get_client_config(config: Dict[str, Any], username: str) -> Dict[str, Any]:
    """
    Get the appropriate OAuth client config for an account.
    
    Args:
        config (Dict[str, Any]): The credentials configuration.
        username (str): The YouTube account username/email.
    
    Returns:
        Dict[str, Any]: The OAuth client configuration.
    
    Raises:
        ValueError: If the client configuration is not found.
    """
    mapping = config.get('account_to_client_mapping', {})
    client_key = mapping.get(username, 'default_client')
    
    if client_key not in config:
        raise ValueError(
            f"OAuth client '{client_key}' not found in credentials config for account: {username}"
        )
    
    return config[client_key]


def create_temp_client_secret(client_config: Dict[str, Any]) -> str:
    """
    Create a temporary client_secret.json file for a specific OAuth client.
    
    Args:
        client_config (Dict[str, Any]): The OAuth client configuration.
    
    Returns:
        str: Path to the temporary file.
    """
    temp_file = tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.json',
        delete=False,
        dir='.'
    )
    
    client_secret_data = {'installed': client_config}
    json.dump(client_secret_data, temp_file)
    temp_file.close()
    
    return temp_file.name


def cleanup_temp_file(file_path: str) -> None:
    """
    Clean up a temporary file.
    
    Args:
        file_path (str): Path to the file to delete.
    """
    if os.path.exists(file_path):
        os.remove(file_path)


def authenticate(
    username: str,
    credentials_config: Dict[str, Any],
    token_dir: str = 'secret',
) -> Any:
    """
    Authenticate with YouTube API using OAuth 2.0 for a specific account.
    
    Args:
        username (str): The YouTube account username/email.
        credentials_config (Dict[str, Any]): The credentials configuration.
        token_dir (str): Directory to store authentication tokens.
    
    Returns:
        Resource: Authenticated YouTube API service object.
    
    Raises:
        Exception: If authentication fails or required libraries are not installed.
    """
    creds = None
    token_file = os.path.join(token_dir, f'token_{username}.pickle')

    # Import Google API libraries lazily
    try:
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
    except ImportError as ie:
        raise Exception(
            "\n❌ Missing required Google API libraries.\n\n"
            "Install them with:\n\n"
            "    pip install --upgrade google-api-python-client "
            "google-auth-httplib2 google-auth-oauthlib\n\n"
            f"Original ImportError: {ie}"
        )
    
    try:
        # Create token directory if it doesn't exist
        os.makedirs(token_dir, exist_ok=True)
        
        # Get the appropriate OAuth client for this account
        client_config = get_client_config(credentials_config, username)
        temp_secret_file = create_temp_client_secret(client_config)
        
        try:
            # Load saved credentials if they exist
            if os.path.exists(token_file):
                with open(token_file, 'rb') as token:
                    creds = pickle.load(token)
            
            # If credentials are invalid or don't exist, get new ones
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    print("🔄 Refreshing expired credentials...")
                    creds.refresh(Request())
                else:
                    print("🔐 Starting OAuth authentication...")
                    print("📋 A browser window will open for authentication.")
                    try:
                        flow = InstalledAppFlow.from_client_secrets_file(
                            temp_secret_file, SCOPES)
                        creds = flow.run_local_server(
                            port=0,
                            open_browser=True,
                            prompt='consent'
                        )
                        print("✅ Authentication successful!")
                    except Exception as oauth_error:
                        raise _handle_oauth_error(oauth_error, username)
                
                # Save credentials for future use
                os.makedirs(token_dir, exist_ok=True)
                with open(token_file, 'wb') as token:
                    pickle.dump(creds, token)
            
            return build('youtube', 'v3', credentials=creds)
            
        finally:
            # Clean up temporary client secret file
            cleanup_temp_file(temp_secret_file)
        
    except Exception as e:
        raise Exception(
            f"\n❌ Authentication failed: {str(e)}\n"
            "Please check your credentials and try again."
        )


def _handle_oauth_error(error: Exception, username: str) -> Exception:
    """
    Handle specific OAuth errors with helpful solutions.
    
    Args:
        error (Exception): The OAuth error that occurred.
        username (str): The YouTube account username/email.
    
    Returns:
        Exception: A new exception with helpful error message.
    """
    error_str = str(error)
    
    if "access_denied" in error_str:
        return Exception(
            f"\n❌ OAuth Access Denied Error!\n\n"
            "🔧 POSSIBLE SOLUTIONS:\n"
            "1. Make sure you created a 'Desktop application' OAuth client (not Web application)\n"
            "2. Verify your Google Cloud project has YouTube Data API v3 enabled\n"
            "3. Check if your OAuth consent screen is properly configured:\n"
            "   - Go to 'OAuth consent screen' in Google Cloud Console\n"
            "   - Add your email as a test user if app is in testing mode\n"
            "   - Make sure required scopes are added\n"
            "4. Try creating a new OAuth client ID as 'Desktop application'\n"
            "5. Download fresh credentials and replace credentials_config.json\n\n"
            f"Original error: {error_str}"
        )
    elif "state" in error_str.lower():
        return Exception(
            f"\n❌ OAuth State Mismatch Error (CSRF Warning)!\n\n"
            "This happens when multiple authentication attempts occur too quickly.\n\n"
            "🔧 SOLUTIONS:\n"
            "1. Close all browser tabs with Google login\n"
            "2. Clear browser cookies for accounts.google.com\n"
            "3. Wait a few seconds before running the script again\n"
            "4. Try running the script once more\n\n"
            f"Original error: {error_str}"
        )
    else:
        return error
