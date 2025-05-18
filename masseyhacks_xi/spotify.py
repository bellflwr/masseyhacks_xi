from dataclasses import dataclass, field
from typing import Any

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


def select_image_url(images: list[dict], min_size: int | None = None) -> str:
    if min_size is None:
        return images[0]["url"]
    for img in reversed(images):
        if img["height"] >= min_size:
            return img["url"]

    return images[0]["url"]


def search_album(album_name, limit=10):
    results = sp.search(q=album_name, type="album", limit=limit)
    albums = results["albums"]["items"]
    if not albums:
        return "No albums found"
    albums_searched = []
    for album in albums:
        total_time = 0
        image_url = select_image_url(album["images"], 64)

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
                name=album["name"],
                id=album["id"],
                artist=album["artists"][0]["name"],
                record_label="",
                release_date=album["release_date"],
                total_tracks=album["total_tracks"],
                image_url=image_url,
                tracks=track_list,
                total_time=total_time,
            )
        )

    return albums_searched


def search_song(song_name: Any, limit: int = 10) -> list[Song]:
    results = sp.search(q=song_name, type="track", limit=limit)
    songs = results["tracks"]["items"]
    if not songs:
        raise Exception("No songs found.")
    songs_searched = []
    for song in songs:
        songs_searched.append(
            Song(
                name=song["name"],
                id=song["id"],
                artist=song["artists"][0]["name"],
                duration_ms=song["duration_ms"],
                preview_url=song["preview_url"],
                image_url=select_image_url(song["album"]["images"], 64),
                times_played=song.get("popularity", 0),
                release_date=song["album"]["release_date"],
                record_label="",
            )
        )
    return songs_searched


def get_album(album_id: Any) -> Album:
    album_data = sp.album(album_id)
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
            image_url=album_data["images"][0]["url"],
            times_played=track.get("popularity", 0),
            release_date=album_data["release_date"],
            record_label=album_data["label"],
        )
        track_list.append(song)
    return Album(
        name=album_data["name"],
        id=album_data["id"],
        artist=album_data["artists"][0]["name"],
        record_label=album_data["label"],
        release_date=album_data["release_date"],
        total_tracks=album_data["total_tracks"],
        image_url=album_data["images"][0]["url"],
        tracks=track_list,
        total_time=total_time,
    )


def get_song(song_id: Any) -> Song:
    song_data = sp.track(song_id)
    album_id = song_data["album"]["id"]
    album_data = sp.album(album_id)

    return Song(
        name=song_data["name"],
        id=song_data["id"],
        artist=song_data["artists"][0]["name"],
        duration_ms=song_data["duration_ms"],
        preview_url=song_data["preview_url"],
        image_url=song_data["album"]["images"][0]["url"],
        times_played=song_data.get("popularity", 0),
        release_date=song_data["album"].get("release_date", ""),
        record_label=album_data.get("label", "Unknown"),
    )
