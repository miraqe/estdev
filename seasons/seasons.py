from datetime import datetime
import inflect
import sys

def main():
    try:
        birth_date = datetime.strptime(input("Date of birth: "), '%Y-%m-%d')
    except ValueError:
        raise sys.exit('Invalid date format')

    p = inflect.engine()
    today = datetime.today()

    if birth_date > today:
        raise sys.exit('Birthday cannot be in the future')

    years = today.year - birth_date.year
    if (birth_date.month, birth_date.day) > (today.month, today.day):
        years -= 1

    minutes = int((today - birth_date).total_seconds() / 60)

    output = p.number_to_words(minutes, andword="", zero="zero").capitalize()
    output += " minute" + ("s" if minutes != 1 else "")

    if years == 0:
        print(output)
        return

    output = p.number_to_words(years, andword="", zero="zero").capitalize()
    output += " year" + ("s" if years != 1 else "") + ", " + output
    print(output)

if __name__ == "__main__":
    main()
