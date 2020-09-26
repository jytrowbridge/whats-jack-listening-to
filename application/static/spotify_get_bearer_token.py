import base64
from dotenv import load_dotenv
import os
from request_funcs import put_request

load_dotenv()
BASE_URL = 'https://accounts.spotify.com/api/token'
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')


def get_bearer_token():
    auth_str = f'{CLIENT_ID}:{CLIENT_SECRET}'
    b64_auth_str = base64.urlsafe_b64encode(auth_str.encode()).decode()

    headers = {'Authorization': f'Basic {b64_auth_str}'}
    body = {'grant_type': 'client_credentials'}

    r = put_request(BASE_URL, headers=headers, body=body)
    print(r.json()['access_token'])


if __name__ == "__main__":
    get_bearer_token()
