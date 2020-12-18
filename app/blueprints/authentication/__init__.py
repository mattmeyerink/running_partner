"""Blueprint for authentication section of the API."""
import flask


auth_bp = flask.Blueprint("auth", __name__, url_prefix="/authentication")

from . import models, routes
