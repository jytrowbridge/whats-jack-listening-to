import sys
[sys.path.append(i) for i in ['.', '..']]
from application.static.lastfm_get_tracks import get_tracks
from application.static.spotify_get_track import get_track_url


def get_recent_tracks():
    tracks = get_tracks()
    cleaned_tracks = []

    currently_playing = False

    for track in tracks:
        cleaned_track = {}
        cleaned_track['artist'] = track['artist']['name']
        cleaned_track['song_title'] = track['name']
        cleaned_track['loved'] = track['loved'] == "1"
        cleaned_track['album_name'] = track['album']['#text']

        spotify_url = get_track_url(track_title=track['name'], artist_name=track['artist']['name'])
        cleaned_track['spotify_url'] = spotify_url or ''

        for img_dic in track['image']:
            if img_dic['size'] == 'extralarge':
                cleaned_track['album_img_url'] = img_dic['#text']
                break

        if '@attr' in track and track['@attr']['nowplaying']:
            currently_playing = True
            cleaned_tracks = [cleaned_track]
            break

        cleaned_tracks.append(cleaned_track)

    return [cleaned_tracks, currently_playing]


if __name__ == "__main__":
    print(get_recent_tracks())
