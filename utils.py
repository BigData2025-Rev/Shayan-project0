def validate_int_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                raise ValueError
            return value
        except ValueError:
            print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")

def validate_date_input(prompt):
    from datetime import datetime
    while True:
        date_str = input(prompt).strip()
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
