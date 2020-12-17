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
