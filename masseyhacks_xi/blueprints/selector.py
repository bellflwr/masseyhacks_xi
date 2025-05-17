from flask import Blueprint, jsonify, render_template, request

selector = Blueprint("selector", __name__)


@selector.route("/")
def selector_page():
    return render_template("selector.html")


def search_for_album(search: str) -> list[str]:
    return ["Polygondwanaland", "Asfalt", "Paces of Places"]


def search_for_song(search: str) -> list[str]:
    return ["Energy Flash", "Life in Reverse", "ილუზია"]


@selector.route("/search/")
def search():
    search_kind = request.args.get("kind")
    search_value = request.args.get("value")

    if search_kind == "album":
        items = search_for_album(search_value)
    elif search_kind == "song":
        items = search_for_song(search_value)
    else:
        raise Exception(f"{search_kind} is not a valid search kind!")

    return jsonify(items)
