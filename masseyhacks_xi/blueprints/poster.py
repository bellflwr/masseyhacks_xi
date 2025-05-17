from flask import Blueprint, render_template

poster = Blueprint("poster", __name__)


@poster.route("/")
def poster_page():
    return render_template("poster.html")
