import sys
from datetime import date, datetime



def get_birthdate():
    """Prompts the user for their birthdate and returns a date object."""
    birthdate_str = input("What's your birthdate (YYYY-MM-DD)? ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit()
    return birthdate


def get_age_in_minutes(birthdate, today):
    """Returns the age in minutes as an integer, given the birthdate and today's date."""
    days_in_year = 365
    minutes_in_day = 24 * 60
    total_days = (today - birthdate).days
    leap_days = sum(1 for year in range(birthdate.year, today.year) if date(year, 2, 29) <= today)
    total_minutes = (total_days - leap_days) * minutes_in_day
    return total_minutes


def main():
    today = date(2000, 1, 1)
    birthdate = get_birthdate()
    age_in_minutes = get_age_in_minutes(birthdate, today)
    p = inflect.engine()
    age_in_words = p.number_to_words(round(age_in_minutes))
    print(age_in_words.replace("-", " ").replace(" and", ""))


if __name__ == "__main__":
    main()
