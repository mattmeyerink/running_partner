"""Routes for API calls regarding training plans."""
import flask
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from . import training_bp
from .models import TrainingPlan, CustomPlan
from app.blueprints.runs.models import Run


@training_bp.route("/all_plans", methods=["GET"])
@jwt_required
def get_all_plans():
    """
    Outputs training plan data
    [GET] /all_plans
    """
    all_plans_obj = TrainingPlan.query.all()
    plans = []
    for plan in all_plans_obj:
        plans.append(plan.to_dict())

    return flask.jsonify(plans)

@training_bp.route("/<int:id>", methods=["GET"])
@jwt_required
def get_plan(id):
    """
    Ouputs all data for a specific training plan
    [GET] /<int:id>
    """
    plan = TrainingPlan.query.get(id)
    return flask.jsonify(plan.to_dict())

@training_bp.route("/add_plan/<int:user_id>", methods=["POST"])
@jwt_required
def add_plan(user_id):
    """
    Create a custom plan for the user.
    [POST] /add_plan/<int:user_id>
    """
    # Verify the user with the token
    if (str(user_id) != get_jwt_identity()):
        return flask.Response(status=403)

    data = flask.request.json

    plan = CustomPlan()
    plan.from_dict(data)
    plan.save()

    return flask.Response(status=201)

@training_bp.route("/custom_plans/<int:user_id>", methods=["GET"])
#@jwt_required
def get_custom_plan(user_id):
    """
    Get all of the custom plans for a specific user.
    Also returns all of the runs for the user for use on each plan page
    [GET] /custom_plans/<int:user_id>
    """
    # Verify the user with the passed token
    # if (str(user_id) != get_jwt_identity()):
    #     return flask.Response(status=403)

    # Get all of the plans under the current_user's account
    plans_raw = CustomPlan.query.filter_by(user_id=user_id).all()

    # Create output array of all plans
    plans = []
    for plan in plans_raw:
        plans.append(plan.to_dict())
    
    # Sort the list in descending order of creation
    plans.sort(key=lambda x: x["created_on"], reverse=True)

    # Query the db for all of the users runs
    run_objects = Run.query.filter_by(user_id=user_id)

    # Convert the objects to dicionaries to be returned
    runs = []
    for run in run_objects:
        runs.append(run.to_dict())
    
    # Sort the list in decending order
    runs.sort(key=lambda x: x["created_on"], reverse=True)

    # Package the runs in one dictionary
    output = {
        "plans": plans,
        "runs": runs
    }

    return flask.jsonify(output)

@training_bp.route("/custom_plan/<int:plan_id>", methods=["GET"])
@jwt_required
def get_custom_plan_data(plan_id):
    """
    Get custom plan data for a specific plan.
    [GET] /custom_plans/<int:plan_id>
    """
    plan = CustomPlan.query.get(plan_id)

    # Verify the token user matches the plan's owner
    if (str(plan.user_id) != get_jwt_identity()):
        return flask.Response(status=403)

    return flask.jsonify(plan.to_dict())

@training_bp.route("/custom_plan/delete/<int:plan_id>", methods=["DELETE"])
@jwt_required
def delete_custom_plan(plan_id):
    """
    Delete a custom plan from the db.
    [DELETE] /custom_plans/<int:plan_id>
    """
    plan = CustomPlan.query.get(plan_id)

    # Verify the token user matches the plan's owner
    if (str(plan.user_id) != get_jwt_identity()):
        return flask.Response(status=403)

    plan.remove()
    return flask.Response(status=200)

@training_bp.route("/custom_plan/edit/<int:id>", methods=["POST"])
@jwt_required
def edit_custom_plan(id):
    """
    Edit a custom plan in the db.
    [POST] /custom_plan/edit/<int:id>
    """
    data = flask.request.json

    plan = CustomPlan.query.get(id)

    # Verify the token user matches the plan's owner
    if (str(plan.user_id) != get_jwt_identity()):
        return flask.Response(status=403)

    plan.plan = data["plan"]
    plan.race_name = data["race_name"]
    db.session.commit()

    return flask.Response(status=200)
