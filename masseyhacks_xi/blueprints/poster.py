from flask import Blueprint, render_template
from masseyhacks_xi import spotify

poster = Blueprint("poster", __name__)


@poster.route("/")
def poster_page():
    return render_template("poster.html")
