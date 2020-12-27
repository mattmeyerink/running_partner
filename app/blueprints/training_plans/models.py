"""Contains the db model for a training plan."""
from app import db
from datetime import datetime as dt


class TrainingPlan(db.Model):
    """Represents summary information for a training plan."""
    __tablename__ = "training_plans"
    id = db.Column(db.Integer, primary_key=True)
    race_length = db.Column(db.Float)
    race_name = db.Column(db.String(50))
    difficulty = db.Column(db.String(50))
    frequency = db.Column(db.Integer)
    plan_length = db.Column(db.Integer)
    plan = db.Column(db.String())

    def __repr__(self):
        return f"<Plan: {self.race_length} | {self.difficulty}>"

    def save(self):
        """Commit the training plan to the db."""
        db.session.add(self)
        db.session.commit()

    def from_dict(self, data):
        """Create a new plan from a dictionary of plan information."""
        for field in ["race_length", "race_name", "difficulty", "frequency",
                      "plan_length"]:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        """Outputs the object data into a dictionary. Used to jsonify it."""
        data = {
            "id": self.id,
            "race_length": self.race_length,
            "race_name": self.race_name,
            "difficulty": self.difficulty,
            "frequency": self.frequency,
            "plan_length": self.plan_length,
            "plan": self.plan
        }
        return data

class CustomPlan(db.Model):
    """Represents summary information for a training plan."""
    __tablename__ = "custom_training_plans"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    difficulty = db.Column(db.String(50))
    race_name = db.Column(db.String(100))
    plan_length = db.Column(db.Integer)
    plan = db.Column(db.String())
    created_on = db.Column(db.DateTime, default=dt.utcnow)

    def __repr__(self):
        return f"<CustomPlan: {self.id} | {self.race_name}>"

    def save(self):
        """Commit the traing plan to the db."""
        db.session.add(self)
        db.session.commit()

    def from_dict(self, data):
        """Create a new training plan in the db from a dictionary."""
        for field in ["user_id", "difficulty", "race_name", "plan_length", "plan"]:
            if field in data:
                setattr(self, field, data[field])
    
    def to_dict(self):
        """Outputs the object data into a dictionary. Used to jsonify it."""
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "difficulty": self.difficulty,
            "race_name": self.race_name,
            "plan_length": self.plan_length,
            "plan": self.plan
        }
        return data
