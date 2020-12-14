"""Script to populate the db with training plans."""
from ../models import TrainingPlan

marathon_easy = TrainingPlan()
marathon_easy_dict = {
    "race_length": 26.2,
    "race_name": "marathon",
    "difficulty": "beginner",
    "frequency": 5,
    "plan_length": 16
}
marathon_easy.from_dict(marathon_easy_dict)
marathon.save()
