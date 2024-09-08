import requests
import json
import os

def get_normal_config():
    return {
        'password': os.environ.get('password'),
        'host': os.environ.get('host'),
        'port': os.environ.get('port'),
        'weatherkey': os.environ.get('weatherkey')
    }

def get_config_details():
    # Replace these with your actual HCP Client ID and Secret
    HCP_CLIENT_ID = os.environ.get('hcp_client_id')
    HCP_CLIENT_SECRET = os.environ.get('hcp_secret')

    # Define the URL and headers
    url = "https://auth.idp.hashicorp.com/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Define the payload
    payload = {
        "client_id": HCP_CLIENT_ID,
        "client_secret": HCP_CLIENT_SECRET,
        "grant_type": "client_credentials",
        "audience": "https://api.hashicorp.cloud"
    }

    # Make the request
    response = requests.post(url, headers=headers, data=payload)

    # Extract the access token from the response
    access_token = response.json().get('access_token')

    # Replace with your actual HCP API token, organization ID, project ID, and app name
    HCP_API_TOKEN = access_token
    organization_id = os.environ.get('organization_id')
    project_id = os.environ.get('project_id')
    app_name = os.environ.get('app_name')

    # Define the URL
    url = f"https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/{organization_id}/projects/{project_id}/apps/{app_name}/open"

    # Define the headers
    headers = {
        "Authorization": f"Bearer {HCP_API_TOKEN}"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        secrets = response.json()
        # Pretty-print the JSON response
        #print(json.dumps(secrets, indent=4))
        kv_pairs = {}
        for item in secrets.get('secrets', []):
            name = item.get('name')
            value = item.get('version', {}).get('value')
            if name and value:
                kv_pairs[name] = value
        return kv_pairs
    else:
        print(f"Failed to retrieve secrets. Status code: {response.status_code}")
        print(response.text)
        return {}