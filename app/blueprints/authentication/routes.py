import flask
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
from app import db
from . import auth_bp
from .models import User
from .reset_password_email import reset_password_email

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

    return flask.Response(status=201)

@auth_bp.route("/login", methods=["POST"])
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
        # Output the user's data to a dict
        user_data = user[0].to_dict()

        # Set up API access token
        expires = timedelta(hours=1)
        access_token = create_access_token(identity=str(user_data["id"]),
                expires_delta=expires)
        user_data["token"] = access_token
        return flask.jsonify(user_data), 200

    # Return 401: Unauthorized
    return flask.abort(401)

@auth_bp.route("/get_user_data/<int:id>", methods=["GET"])
@jwt_required
def get_user_data(id):
    """Route to get account data for a user."""
    # Retrieve the user id from the request
    user = User.query.get(id)
    user_data = user.to_dict()

    # Set up API access token
    expires = timedelta(hours=1)
    access_token = create_access_token(identity=str(user_data["id"]),
            expires_delta=expires)
    user_data["token"] = access_token
    return flask.jsonify(user_data)

@auth_bp.route("/edit_profile", methods=["POST"])
@jwt_required
def edit_profile():
    """Route to update account information."""
    # Retrive the new user data
    data = flask.request.json

    # Pull the user id from the request
    id = data["id"]
    user = User.query.get(id)

    # Update the user data in the db
    user.from_dict(data)
    db.session.commit()

    return flask.Response(status=200)

@auth_bp.route("/delete_account/<int:id>", methods=["DELETE"])
@jwt_required
def delete_account(id):
    """Delete the users account from the db."""
    user = User.query.get(id)
    user.remove()

    return flask.Response(status=200)

@auth_bp.route("/set_active_plan", methods=["POST"])
@jwt_required
def set_active_plan():
    """Set the active plan of a given user."""
    data = flask.request.json

    # Pull the user id and plan id from the request
    user_id = data["user_id"]
    plan_id = data["plan_id"]

    # Retrive user from the database
    user = User.query.get(user_id)

    # Set the users active plan as the passed plan id
    user.active_plan = plan_id
    db.session.commit()

    return flask.Response(status=200)

@auth_bp.route("/initiate_password_reset", methods=["POST"])
def initiate_password_reset():
    """Initiate a password reset by confirming given email."""
    data = flask.request.json
    email = data["email"]

    user = User.query.filter_by(email=email).all()

    if (user):
        reset_password_email(email, user.id)
        return flask.Response(status=200)

    # Return not found if no user with that email found
    return flask.Response(status=404)
