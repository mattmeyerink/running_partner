"""Routes for runs section of the API."""
import flask
from . import runs_bp
from .models import Run


@runs_bp.route("/add_run", methods=["POST"])
def add_run():
    """
    Adds a training plan to the db.
    [POST] /add_run
    """
    data = flask.request.json

    run = Run()
    run.from_dict(data)
    run.save()

    return flask.Response(status=201)
