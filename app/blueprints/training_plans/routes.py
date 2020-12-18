"""Routes for API calls regarding training plans."""
import flask
from . import training_bp
from .models import TrainingPlan


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
