"""Script to populate the db with training plans."""
from ../models import TrainingPlan

marathon_easy = TrainingPlan()
marathon_easy_dict = {
    "race_length": 26.2,
    "race_name": "marathon",
    "difficulty": "beginner",
    "frequency": 4,
    "plan_length": 18
}
marathon_easy.from_dict(marathon_easy_dict)
marathon.save()

marathon_intermediate = TrainingPlan()
marathon_intermediate_dict = {
    "race_length": 26.2,
    "race_name": "marathon",
    "difficulty": "intermediate",
    "frequency": 6,
    "plan_length": 16
}
marathon_intermediate.from_dict(marathon_intermediate_dict)
marathon_intermediate.save()

marathon_advanced = TrainingPlan()
marathon_advanced_dict = {
    "race_length": 26.2,
    "race_name": "marathon",
    "difficulty": "beginner",
    "frequency": 7,
    "plan_length": 16
}
marathon_advanced.from_dict(marathon_advanced_dict)
marathon_advanced.save()
