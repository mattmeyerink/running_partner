"""Routes for API calls regarding training plans."""
import flask
from . import training_bp
from .models import TrainingPlan, CustomPlan


@training_bp.route("/all_plans", methods=["GET"])
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
def get_plan(id):
    """
    Ouputs all data for a specific training plan
    [GET] /<int:id>
    """
    plan = TrainingPlan.query.get(id)
    return flask.jsonify(plan.to_dict())

@training_bp.route("/add_plan/<int:user_id>", methods=["POST"])
def add_plan(user_id):
    """
    Create a custom plan for the user.
    [POST] /add_plan/<int:user_id>
    """
    data = flask.request.json

    plan = CustomPlan()
    plan.from_dict(data)
    plan.save()

    return flask.Response(status=201)
