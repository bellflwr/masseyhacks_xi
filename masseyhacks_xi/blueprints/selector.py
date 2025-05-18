from dataclasses import asdict

from flask import Blueprint, jsonify, render_template, request

from masseyhacks_xi.spotify import search_album, search_song

selector = Blueprint("selector", __name__)


@selector.route("/")
def selector_page():
    return render_template("selector.html")


@selector.route("/search/")
def search():
    search_kind = request.args.get("kind")
    search_value = request.args.get("value")

    if search_kind == "album":
        items = search_album(search_value, 15)
    elif search_kind == "song":
        items = search_song(search_value, 15)
    else:
        raise Exception(f"{search_kind} is not a valid search kind!")

    return jsonify([asdict(item) for item in items])
