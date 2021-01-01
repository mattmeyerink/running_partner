"""Blueprint for the runs section of the API."""
import flask


runs_bp = flask.Blueprint("runs", __name__, url_prefix="/runs")

from . import models, routes
