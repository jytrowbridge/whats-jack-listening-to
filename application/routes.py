from application import app
from flask import render_template
# from application.static.get_tracks import get_tracks
# from application.static.spotify_get_track import get_track_url
from application.static.get_recent_tracks import get_recent_tracks

@app.route('/')
def index():
    [tracks, currently_playing] = get_recent_tracks()

    return render_template(
            'index.html',
            tracks=tracks,
            # currently_playing=currently_playing
            currently_playing=False
        )
