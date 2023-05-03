from datetime import date
import sys
import re


try:
    birthdate = date.fromisoformat(input("Date of Birth: "))
except:
    sys.exit("Invalid date")
difference = date.today() - birthdate
age_minutes = difference.days * 24 * 60
p = inflect.engine()
print(p.number_to_words(age_minutes).capitalize() + " minutes")
    sys.exit("Invalid Date")


if __name__ == "__main__":
    main()