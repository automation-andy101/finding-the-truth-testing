import requests
from utilities.configurations import get_api_config

class APIClient:
    def __init__(self):
        self.OAUTH_BASE_URL = get_api_config()['TEST']['OAUTH_API_BASE_URL']
        self.API_BASE_URL1 = get_api_config()['TEST']['API_BASE_URL1']
        self.BOOKMARK_RESOURCE = get_api_config()['TEST']['BOOKMARK_RESOURCE']
        self.API_CODE = get_api_config()['TEST']['API_CODE']

    def get_bearer_token(self, username, password):
        url = f"{self.OAUTH_BASE_URL}/oauth/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "password",
            "username": username,
            "password": password
        }
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json().get("access_token")

    def get_bookmarks(self, bearer_token, session_uuid):
        url = f"{self.BASE_URL}/{self.RESOURCE}/{session_uuid}/{self.API_CODE}"
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def post_bookmarks(self, bearer_token, session_uuid, payload):
        url = f"{self.BASE_URL}/{self.RESOURCE}/{session_uuid}/{self.API_CODE}"
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        return response.json()