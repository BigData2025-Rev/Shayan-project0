from datetime import datetime

class Exercise:
    def __init__(self, exercise_type, duration, calories, date=None):
        self.exercise_type = exercise_type
        self.duration = duration  # in minutes
        self.calories = calories  # in kcal
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            "exercise_type": self.exercise_type,
            "duration": self.duration,
            "calories": self.calories,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Exercise(data["exercise_type"], data["duration"], data["calories"], data["date"])
