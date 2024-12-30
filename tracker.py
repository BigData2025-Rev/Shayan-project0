import os
import json
from exercise import Exercise

class FitnessTracker:
    def __init__(self, user, filename='data/fitness_data.json'):
        self.filename = filename
        self.user = user
        self.exercises = self.load_data()

    def ensure_file_exists(self):
        # Create the `data/` directory and JSON file if they don't exist
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)

    def load_data(self):
        self.ensure_file_exists()
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Exercise.from_dict(entry) for entry in data if entry["user"] == self.user]
        except FileNotFoundError:
            return []

    def save_data(self):
        self.ensure_file_exists()
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        user_data = [exercise.to_dict() | {"user": self.user} for exercise in self.exercises]
        data = [entry for entry in data if entry["user"] != self.user] + user_data
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def add_exercise(self, exercise_type, duration, calories):
        new_exercise = Exercise(exercise_type, duration, calories)
        self.exercises.append(new_exercise)
        self.save_data()
        print("Exercise added successfully!")

    def edit_exercise(self, index, exercise_type, duration, calories):
        try:
            self.exercises[index] = Exercise(exercise_type, duration, calories)
            self.save_data()
            print("Exercise updated successfully!")
        except IndexError:
            print("Invalid index. Please try again.")

    def delete_exercise(self, index):
        try:
            del self.exercises[index]
            self.save_data()
            print("Exercise deleted successfully!")
        except IndexError:
            print("Invalid index. Please try again.")

    def view_exercises(self):
        if not self.exercises:
            print("No exercises logged yet.")
            return
        for idx, exercise in enumerate(self.exercises, start=1):
            print(f"{idx}. {exercise.date}: {exercise.exercise_type} - {exercise.duration} min, {exercise.calories} kcal")

    def filter_by_date(self, date):
        filtered = [exercise for exercise in self.exercises if exercise.date == date]
        if filtered:
            for exercise in filtered:
                print(f"{exercise.date}: {exercise.exercise_type} - {exercise.duration} min, {exercise.calories} kcal")
        else:
            print("No exercises found for the specified date.")

    def calories_by_type(self):
        stats = {}
        for exercise in self.exercises:
            stats[exercise.exercise_type] = stats.get(exercise.exercise_type, 0) + exercise.calories
        for exercise_type, calories in stats.items():
            print(f"{exercise_type}: {calories} kcal")
