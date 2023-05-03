from datetime import date, datetime, timedelta
import inflect
import sys

def main():
    try:
        birth_date = datetime.strptime(input("Date of birth: "), '%Y-%m-%d')
    except ValueError:
        sys.exit('Invalid date format. Please enter a date in the format YYYY-MM-DD')
    except:
        sys.exit('Invalid date')

    check_birthday(birth_date)
    p = inflect.engine()
    today = datetime.strptime("2000-01-01", "%Y-%m-%d")
    time_lapse = today - birth_date
    minutes = time_lapse / timedelta(minutes=1)
    minutes = int(minutes)
    output = p.number_to_words(minutes, andword="")
    output = output.capitalize() + " minutes"
    return output

def check_birthday(birth_date):
    if birth_date > datetime.now():
        raise ValueError('Birth date is in the future')
    elif birth_date.year < 1900:
        raise ValueError('Birth year is before 1900')
    else:
        return True

if __name__ == "__main__":
    print(main())
