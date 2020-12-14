import flask
from config import Config


def create_app():
    """Creates an instance of the application."""
    # Initialize the app
    app = flask.Flask(__name__)

    # Add the config settings
    app.config.from_object(Config)
