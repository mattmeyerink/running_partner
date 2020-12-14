"""Contains the db model for a training plan."""
from app import db


class TrainingPlan(db.Model):
    """Represents summary information for a training plan."""
    __tablename__ = "training_plans"
    id = db.Column(db.Integer, primary_key=True)
    race_length = db.Column(db.Float)
    race_name = db.Column(db.String(50))
    difficulty = db.Column(db.String(50))
    frequency = db.Column(db.Integer)
    plan_length = db.Column(db.Integer)

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

class BeginnerMarathon(db.Model):
    """Holds the data for each day's training"""
    __tablename__ = "beginner_marathon"
    week = db.Column(db.Integer, primary_key=True)
    monday = db.Column(db.Integer)
    tuesday = db.Column(db.Integer)
    wednesday = db.Column(db.Integer)
    thursday = db.Column(db.Integer)
    friday = db.Column(db.Integer)
    saturday = db.Column(db.Integer)
    sunday = db.Column(db.Integer)

    def __repr__(self):
        return f"<Week {self.week}>"

    def save(self):
        """Commit the training plan to the db."""
        db.session.add(self)
        db.session.commit()

    def from_dict(self, data):
        """Create a new week of runs from a dictionary of runs."""
        for field in ["monday", "tuesday", "wednesday", "thursday", "friday",
                      "saturday", "sunday"]:
            if field in data:
                setattr(self, field, data[field])
    
