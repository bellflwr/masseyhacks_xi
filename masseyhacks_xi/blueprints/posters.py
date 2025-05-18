from flask import Blueprint, render_template

from masseyhacks_xi.spotify import get_album, get_song

posters = Blueprint("posters", __name__)


@posters.route("/album/<id>")
def albums_page(id):
    album = get_album(id)
    return render_template("album_posters.html", album=album)


@posters.route("/single/<id>")
def singles_page(id):
    song = get_song(id)
    return render_template("single_posters.html", song=song)
