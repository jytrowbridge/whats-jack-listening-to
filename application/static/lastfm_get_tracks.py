from dotenv import load_dotenv
import hashlib
import json
import os
import sys
[sys.path.append(i) for i in ['.', '..']]
from application.static.request_funcs import get_request


load_dotenv()
API_KEY = os.getenv('LASTFM_API_KEY')
BASE_URL = 'http://ws.audioscrobbler.com/2.0/?'


def build_sig(method_name):
    sign_str = 'api_key' + API_KEY + f'method{method_name}' + f'sk{SESSION_KEY}' + SECRET
    return hashlib.md5(sign_str.encode()).hexdigest()


def get_tracks():
    params = {
        'method': 'user.getrecenttracks',
        'api_key': API_KEY,
        'format': 'json',
        'user': 'hpdwq',
        'limit': 3,
        'extended': 1,
    }

    return get_request(BASE_URL, params=params).json()['recenttracks']['track']


if __name__ == "__main__":
    print(json.dumps(get_tracks(), indent=2))
