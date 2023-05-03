
from datetime import datetime
import inflect
import sys

def check_birthday(birth_date):
    try:
        datetime.strptime(str(birth_date), '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date")
    today = datetime.strptime("2000-01-01", "%Y-%m-%d")
    if birth_date > today:
        raise ValueError("Birth date is in the future")
    return True
