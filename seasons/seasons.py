from datetime import date
import inflect
import sys


def get_birthdate():
    """
    Prompt the user for their birthdate and return a date object.
    Exit if the input is not in YYYY-MM-DD format.
    """
    while True:
        try:
            birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
            year, month, day = map(int, birthdate.split("-"))
            return date(year, month, day)
        except ValueError:
            print("Invalid date format. Please try again.")
            continue
        except KeyboardInterrupt:
            sys.exit()


def minutes_since_birth(birthdate):
    """
    Return the number of minutes since the given birthdate.
    """
    now = date.today()
    delta = now - birthdate
    total_minutes = (delta.days * 24 * 60) + (delta.seconds // 60)
    return total_minutes


def main():
    p = inflect.engine()

    birthdate = get_birthdate()
    minutes = minutes_since_birth(birthdate)

    if minutes < 525600:
        print("Less than a year old!")
    elif minutes == 525600:
        print("Five hundred twenty-five thousand, six hundred minutes")
    else:
        years = minutes // 525600
        minutes_remaining = minutes % 525600
        minute_str = p.number_to_words(round(minutes_remaining, -2))
        year_str = p.number_to_words(years) if years > 1 else "one"
        print(f"{year_str} million, {minute_str} minutes")


if __name__ == "__main__":
    main()
