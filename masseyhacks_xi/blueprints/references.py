from flask import Blueprint, render_template

references = Blueprint("references", __name__)

@references.route("/")
def albums_page():
    return render_template("album_posters.html")
