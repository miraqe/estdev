from datetime import datetime, timedelta
import inflect
import sys

def main():
    try:
        birth_date = datetime.strptime(input("Date of birth: "), '%Y-%m-%d')
    except ValueError:
        sys.exit('Invalid date')
    p = inflect.engine()
    today = datetime.strptime("2000-01-01", "%Y-%m-%d")
    check_birthday(birth_date)
    if birth_date > today:
        sys.exit()
    time_lapse = today - birth_date
    minutes = int(time_lapse.total_seconds() // 60)
    output = p.number_to_words(minutes, andword="")
    output = output.capitalize() + " minutes"
    print(output)

def check_birthday(birth_date):
    if birth_date > datetime.now():
        sys.exit('Invalid date')

if __name__ == "__main__":
    main()
