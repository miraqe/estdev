from datetime import datetime
import inflect
import sys

def main():
    try:
        birth_date = datetime.strptime(input("Date of birth: "), '%Y-%m-%d')
    except ValueError:
        print("Invalid date format, please enter date in the format YYYY-MM-DD")
        sys.exit(1)

    today = datetime.now()
    if birth_date > today:
        print("Invalid birthdate, please enter a date that is not in the future.")
        sys.exit(1)

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if months < 0 or (months == 0 and days < 0):
        years -= 1

    p = inflect.engine()
    minutes = (today - birth_date).total_seconds() // 60
    output = p.number_to_words(int(minutes), andword="") + " minutes"
    print(output.capitalize())

if __name__ == "__main__":
    main()
