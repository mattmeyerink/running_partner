import flask
from . import main_bp


@main_bp.route("/")
def show_main():
    return flask.render_template("index.html")
