from flask import Blueprint, render_template

posters = Blueprint("posters", __name__)


@posters.route("/album")
def albums_page():
    return render_template("album_posters.html")


@posters.route("/single")
def singles_page():
    return render_template("single_posters.html")
