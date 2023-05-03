from datetime import date, timedelta
import re
import sys

p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birth_date)
    except:
         sys.exit("Invalid Date")
    date_of_birth = date(int(year), int(month), int(day))
    date_of_today = date.today()
    diff = date_of_today - date_of_birth
    total_minutes = diff.days * 24 *60
    output = p.number_to_words(total_minutes, andword="")
    print(output.capitalize() + " minutes")


def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month,day
        try:
            b = date.fromisoformat(birth)
        except ValueError:
            sys.exit("Invalid date type")
        else:
            #take current date
            today = date.today()
            #substract one from another
            sub = today - b
            total = sub.total_seconds() / 60

        return round(total)

def convert_totext(num):
    return f"{p.number_to_words(num, andword='')} minutes"


if _name_ == "__main__":
    main()