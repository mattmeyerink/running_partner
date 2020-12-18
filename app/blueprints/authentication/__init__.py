"""Blueprint for authentication section of the API."""
import flask


auth_bp = flask.Blueprint("auth", url_prefix="/authentication")

from . import models, routes
