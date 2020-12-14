import flask
from . import training_bp

@training_bp.route("/")
def show_training_plans():
    """Display the training plans in the db."""
    return flask.render_template("all_plans.html")
