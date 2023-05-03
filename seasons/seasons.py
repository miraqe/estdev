from datetime import date, datetime, timedelta
import inflect
import sys

p = inflect.engine()

try:
    birth_date = datetime.strptime(input("Date of birth: "), '%Y-%m-%d')
except:
    raise sys.exit('Invalid date')

def main(birth_date):
    today = datetime.date("2000-01-01")
    time_lapse = today - birth_date
    minutes = time_lapse / timedelta(minutes=1)
    minutes = int(minutes)
    output = p.number_to_words(minutes)
    print(output.capitalize(), "minutes")


if __name__ == "__main__":
    main(birth_date)