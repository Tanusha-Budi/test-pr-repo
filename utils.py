def format_name(first, last):
    return first + " " + last

def calculate_age(birth_year):
    return 2024 - birth_year

def is_valid_email(email):
    if "@" in email:
        return True
    return False