from tracker import FitnessTracker
from utils import validate_int_input, validate_date_input

def main():
    print("Welcome to the Fitness Tracker!")
    user = input("Enter your username: ").strip()
    tracker = FitnessTracker(user)

    while True:
        print("\nFitness Tracker Menu:")
        print("1. Add Exercise")
        print("2. View Exercises")
        print("3. Edit Exercise")
        print("4. Delete Exercise")
        print("5. Filter by Date")
        print("6. Calories Burned by Type")
        print("7. Exit")

        choice = validate_int_input("Choose an option: ", 1, 7)

        if choice == 1:
            exercise_type = input("Enter exercise type: ").strip()
            duration = validate_int_input("Enter duration (in minutes): ", 1)
            calories = validate_int_input("Enter calories burned: ", 1)
            tracker.add_exercise(exercise_type, duration, calories)
        elif choice == 2:
            tracker.view_exercises()
        elif choice == 3:
            tracker.view_exercises()
            index = validate_int_input("Enter the index of the exercise to edit: ", 1, len(tracker.exercises)) - 1
            exercise_type = input("Enter new exercise type: ").strip()
            duration = validate_int_input("Enter new duration (in minutes): ", 1)
            calories = validate_int_input("Enter new calories burned: ", 1)
            tracker.edit_exercise(index, exercise_type, duration, calories)
        elif choice == 4:
            tracker.view_exercises()
            index = validate_int_input("Enter the index of the exercise to delete: ", 1, len(tracker.exercises)) - 1
            tracker.delete_exercise(index)
        elif choice == 5:
            date = validate_date_input("Enter date (YYYY-MM-DD): ")
            tracker.filter_by_date(date)
        elif choice == 6:
            tracker.calories_by_type()
        elif choice == 7:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
