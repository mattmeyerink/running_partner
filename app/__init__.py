"""Contains the create_app function to Initialize and instance of the app."""
import flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


# Create instances of the db

def create_app():
    """Creates an instance of the application."""
    # Initialize the app
    app = flask.Flask(__name__)

    # Add the config settings
    app.config.from_object(Config)

    # Link the db to the app

    # Register the blueprints
    from .blueprints.main import main_bp
    app.register_blueprint(main_bp)

    from .blueprints.training_plans import training_bp
    app.register_blueprint(training_bp)

    # Create the db
    # with app.app_context():
    #     db.create_all()

    return app
