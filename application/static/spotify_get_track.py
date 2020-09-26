import os
from dotenv import load_dotenv
import sys
[sys.path.append(i) for i in ['.', '..']]
from application.static.request_funcs import get_request

load_dotenv()
BEARER_TOKEN = os.getenv('SPOTIFY_BEARER_TOKEN')


def get_track_url(track_title, artist_name):
    headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}
    params = {
        'q': f'track:{track_title} artist:{artist_name}',
        'type': 'track',
        'limit': '1'
    }
    url = 'https://api.spotify.com/v1/search'

    r_raw = get_request(url, headers=headers, params=params)
    r_track = r_raw.json()['tracks']['items'][0]

    r_track_name = r_track['name'].upper()
    r_artist_name = r_track['artists'][0]['name'].upper()

    if r_track_name == track_title.upper() and r_artist_name == artist_name.upper():
        return r_track['external_urls']['spotify']
    else:
        return False


if __name__ == "__main__":
    print(get_track_url('chopped in half', 'obituary'))
