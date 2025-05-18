from flask import Blueprint, render_template

playlist_maker = Blueprint("playlist_maker", __name__)


@playlist_maker.route("/")
def playlist_maker():
    return render_template("playlist_maker.html")