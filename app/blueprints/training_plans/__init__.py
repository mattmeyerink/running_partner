"""Blueprint for the training plans API."""
import flask


training_bp = flask.Blueprint("training", __name__, url_prefix="/training_plans")

from . import routes, models
