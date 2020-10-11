import json
from application import app
from flask import render_template
# from application.static.spotify_get_track import get_track_url
from application.static.get_recent_tracks import get_recent_tracks
from application.static.lastfm_get_tracks import get_tracks
from application.static.spotify_get_bearer_token import get_bearer_token

SPOTIFY_BEARER_TOKEN = get_bearer_token()

@app.route('/')
def index():
    [tracks, currently_playing] = get_recent_tracks(SPOTIFY_BEARER_TOKEN)

    return render_template(
            'index.html',
            tracks=tracks,
            currently_playing=currently_playing
            # currently_playing=False
        )


@app.route('/test_ajax')
def test():
    print('jaaaaaack')
    recent_tracks = get_recent_tracks(SPOTIFY_BEARER_TOKEN)
    return json.dumps(recent_tracks)
