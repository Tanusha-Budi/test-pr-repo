def format_name(first: str, last: str) -> str:
    return f"{first} {last}"

def calculate_age(birth_year: int) -> int:
    from datetime import datetime
    current_year = datetime.now().year
    return current_year - birth_year

def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]