import flask
from app import db
from . import auth_bp
from .models import User


@auth_bp.route("/register", methods=["POST"])
def register_user():
    """Route to register a new user with the db."""
    # Gather the post data
    data = flask.request.json

    # Check if the email is already in the db
    email = data["email"]

    user = User.query.filter_by(email=email).all()
    
    # Return conflict error if the email is already in use
    if user:
        return flask.abort(409)
    
    # Initiate the new user object
    new_user = User()
    new_user.from_dict(data)

    # Retrieve the password from the request and hash the pasword
    password = data["password"]
    new_user.hash_password(password)

    # Save the user session
    new_user.save()

    # Return success created code
    return flask.Response(status=201)

@auth_bp.route("/login", methods=["POST", "GET"])
def login_user():
    """Route to check login information."""
    # Gather the post data
    data = flask.request.json
    email = data["email"]
    password = data["password"]

    # Query the db for a user with that username
    user = User.query.filter_by(email=email).all()
    
    # If the credentials are valid, return the user data
    if user and user[0].check_hashed_password(password):
        return flask.jsonify(user[0].to_dict()), 200
    
    # Return 401: Unauthorized
    return flask.abort(401)

@auth_bp.route("/get_user_data/<int:id>", methods=["GET"])
def get_user_data(id):
    """Route to get account data for a user."""
    user = User.query.get(id)

    return flask.jsonify(user.to_dict())

@auth_bp.route("/edit_profile", methods=["POST"])
def edit_profile():
    """Route to update account information."""
    data = flask.request.json
    id = data["id"]
    user = User.query.get(id)

    user.from_dict(data)
    db.session.commit()

    return flask.Response(status=200)

