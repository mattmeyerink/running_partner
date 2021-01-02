"""Routes for runs section of the API."""
import flask
from . import runs_bp
from .models import Run


@runs_bp.route("/add_run", methods=["POST"])
def add_run():
    """
    Adds a training plan to the db.
    [POST] /add_run
    """
    data = flask.request.json

    run = Run()
    run.from_dict(data)
    run.save()

    return flask.Response(status=201)

@runs_bp.route("/all_runs/<int:user_id>", methods=["GET"])
def get_all_runs(user_id):
    """
    Returns all of the run data for a user.
    [GET] /all_runs/<int:user_id>
    """
    # Query the db for all of the users runs
    run_objects = Run.query.filter_by(user_id=user_id)

    # Convert the objects to dicionaries to be returned
    runs = []
    for run in run_objects:
        runs.append(run.to_dict())

    return flask.jsonify(runs)

@runs_bp.route("/delete_run/<int:id>", methods=["DELTE"])
def delete_run(id):
    """
    Deletes a run from the db by id
    [DELETE] /delete_run/<int:id>
    """
    # Query to get the run to delete
    run = Run.query.get(id)
    run.remove()

    return flask.Response(status=200)
