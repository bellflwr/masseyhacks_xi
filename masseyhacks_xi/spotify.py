import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results["items"]):
#    track = item["track"]
#    print(idx, track["artists"][0]["name"], " – ", track["name"])


def display_album(album_name):
    results = sp.search(q=album_name, type="album")
    albums = results["albums"]["items"]
    if not albums:
        return "No albums found"

    album = albums[0]
    album_info = {
        "name": album["name"],
        "artist": album["artists"][0]["name"],
        "release_date": album["release_date"],
        "total_tracks": album["total_tracks"],
        "image_url": album["images"][0]["url"],
    }
    tracks = sp.album_tracks(album["id"])
    track_list = []
    for track in tracks["items"]:
        track_info = {
            "name": track["name"],
            "duration_ms": track["duration_ms"],
            "preview_url": track["preview_url"],
        }
        track_list.append(track_info)

    return album_info, track_list


print(display_album("Submarine"))
