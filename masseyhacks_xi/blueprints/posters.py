from flask import Blueprint, render_template

from masseyhacks_xi.spotify import get_album, get_song
from datetime import datetime

posters = Blueprint("posters", __name__)


@posters.route("/album/<id>")
def albums_page(id):
    album = get_album(id)
    duration = album.total_time
    pcd = datetime.now().strftime("%Y-%m-%d")
    duration = int(duration / 1000)
    minutes = duration // 60
    seconds = duration % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    duration = f"{minutes}:{seconds}"

    return render_template(
        "album_posters.html", album=album, duration=duration, pcd=pcd
    )


@posters.route("/single/<id>")
def singles_page(id):
    song = get_song(id)
    duration = song.duration_ms
    pcd = datetime.now().strftime("%Y-%m-%d")
    duration = int(duration / 1000)
    minutes = duration // 60
    seconds = duration % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    duration = f"{minutes}:{seconds}"
    return render_template("single_posters.html", song=song, duration=duration, pcd=pcd)
