from dataclasses import asdict, dataclass

from flask import Blueprint, jsonify, render_template, request

selector = Blueprint("selector", __name__)


@selector.route("/")
def selector_page():
    return render_template("selector.html")


@dataclass
class Song:
    title: str
    artists: list[str]
    image_url: str


def search_for_album(search: str) -> list[str]:
    return ["Polygondwanaland", "Asfalt", "Paces of Places"]


def search_for_song(search: str) -> list[Song]:
    return [
        Song(
            "Energy Flash",
            ["Joey Beltram"],
            "https://i.scdn.co/image/ab67616d0000b273215f7aaad42adf6cc9457fd0",
        ),
        Song(
            "Life in Reverse",
            ["blanketdragon", "Mr. Bill"],
            "https://i.scdn.co/image/ab67616d0000b273693f5d7f8ebf8c9aa7c45d60",
        ),
        Song(
            "ილუზია",
            ["ნუ მიეყრდნობით"],
            "https://i.scdn.co/image/ab67616d0000b27331d0f341aa955ba0ab697245",
        ),
    ]


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

    return jsonify([asdict(item) for item in items])
