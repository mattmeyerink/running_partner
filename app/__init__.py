"""Contains the create_app function to Initialize and instance of the app."""
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from config import Config


# Create instances of the db
db = SQLAlchemy()

def create_app():
    """Creates an instance of the application."""
    # Initialize the app
    app = flask.Flask(__name__)
    
    # Allow cross origin requests while API and App still operating on local machine
    CORS(app)
    
    # Add the config settings
    app.config.from_object(Config)

    # Link the db to the app
    db.init_app(app)

    # Register the blueprints
    from .blueprints.authentication import auth_bp
    app.register_blueprint(auth_bp)
    
    from .blueprints.main import main_bp
    app.register_blueprint(main_bp)

    from .blueprints.training_plans import training_bp
    app.register_blueprint(training_bp)

    # Create the db
    with app.app_context():
        db.create_all()

    return app
