from dataclasses import dataclass, field

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


@dataclass
class Song:
    name: str
    id: str
    artist: str
    duration_ms: int
    preview_url: str
    image_url: str
    times_played: int
    release_date: str
    record_label: str


@dataclass
class Album:
    name: str
    id: str
    artist: str
    record_label: str
    release_date: str
    total_tracks: int
    image_url: str
    total_time: int
    tracks: list[Song] = field(repr=False)


scope = "user-library-read"

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def search_album(album_name, limit=10):
    results = sp.search(q=album_name, type="album", limit=limit)
    albums = results["albums"]["items"]
    if not albums:
        return "No albums found"
    albums_searched = []
    for album in albums:
        name = album["name"]
        id = album["id"]
        artist = album["artists"][0]["name"]
        release_date = album["release_date"]
        record_label = ""
        total_tracks = album["total_tracks"]
        image_url = album["images"][0]["url"]
        total_time = 0

        tracks = sp.album_tracks(album["id"])
        track_list = []
        for track in tracks["items"]:
            total_time += track["duration_ms"]
            song = Song(
                name=track["name"],
                id=track["id"],
                artist=track["artists"][0]["name"],
                duration_ms=track["duration_ms"],
                preview_url=track["preview_url"],
                image_url=image_url,
                times_played=track.get("popularity", 0),
                release_date=album["release_date"],
                record_label="",
            )
            track_list.append(song)
        albums_searched.append(
            Album(
                name=name,
                id=id,
                artist=artist,
                record_label=record_label,
                release_date=release_date,
                total_tracks=total_tracks,
                image_url=image_url,
                tracks=track_list,
                total_time=total_time,
            )
        )

    return albums_searched


def search_song(song_name, limit=10):
    results = sp.search(q=song_name, type="track", limit=limit)
    songs = results["tracks"]["items"]
    if not songs:
        return "No songs found"
    songs_searched = []
    # with open("thefog.json", "w") as f:
    #     json.dump(songs[0], f, indent=4)
    for song in songs:
        name = song["name"]
        id = song["id"]
        artist = song["artists"][0]["name"]
        duration_ms = song["duration_ms"]
        preview_url = song["preview_url"]
        image_url = song["album"]["images"][0]["url"]
        times_played = song.get("popularity", 0)
        release_date = song["album"]["release_date"]
        record_label = ""

        songs_searched.append(
            Song(
                name=name,
                id=id,
                artist=artist,
                duration_ms=duration_ms,
                preview_url=preview_url,
                image_url=image_url,
                times_played=times_played,
                release_date=release_date,
                record_label=record_label,
            )
        )
    return songs_searched


def get_album(album_id):
    album = sp.album(album_id)
    name = album["name"]
    id = album["id"]
    artist = album["artists"][0]["name"]
    record_label = album["label"]
    release_date = album["release_date"]
    total_tracks = album["total_tracks"]
    image_url = album["images"][0]["url"]
    total_time = 0

    tracks = sp.album_tracks(album_id)
    track_list = []
    for track in tracks["items"]:
        total_time += track["duration_ms"]
        song = Song(
            name=track["name"],
            id=track["id"],
            artist=track["artists"][0]["name"],
            duration_ms=track["duration_ms"],
            preview_url=track["preview_url"],
            image_url=image_url,
            times_played=track.get("popularity", 0),
            release_date=album["release_date"],
            record_label=album["label"],
        )
        track_list.append(song)
    return Album(
        name=name,
        id=id,
        artist=artist,
        record_label=record_label,
        release_date=release_date,
        total_tracks=total_tracks,
        image_url=image_url,
        tracks=track_list,
        total_time=total_time,
        times_played=album.get("popularity", 0),
    )


def get_song(song_id):
    song = sp.track(song_id)
    name = song["name"]
    id = song["id"]
    artist = song["artists"][0]["name"]
    duration_ms = song["duration_ms"]
    preview_url = song["preview_url"]
    image_url = song["album"]["images"][0]["url"]
    times_played = song.get("popularity", 0)
    release_date = song["album"].get("release_date", "")
    album_details = sp.album(song["album"]["id"])
    record_label = album_details.get("label", "Unknown")

    return Song(
        name=name,
        id=id,
        artist=artist,
        duration_ms=duration_ms,
        preview_url=preview_url,
        image_url=image_url,
        times_played=times_played,
        release_date=release_date,
        record_label=record_label,
    )
