import flask
from . import auth_bp
from .models import User


@auth_bp.route("/register", methods=["POST"])
def register_user():
    """Route to register a new user with the db."""
    # Gather the post data
    data = flask.request.json

    # Check if the email is already in the db
    email = data["email"]

    user = User.query.get(email=email).all()
    
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
    user = User.query.get(email=email).all()[0]
    
    # If the credentials are valid, return the user data
    if user and user.check_hashed_password(password):
        return flask.jsonify(user.to_dict())
    
    # Return 401: Unauthorized
    return flask.abort(401)
