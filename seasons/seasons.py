import sys
from datetime import date, datetime
import inflect

def calculate_age_in_minutes(birthdate):
    today = date.today()
    age_in_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    leap_years = count_leap_years(birthdate.year, today.year)
    days = (today - birthdate).days
    total_minutes = (age_in_years * 365 * 24 * 60) + (leap_years * 24 * 60) + (days * 24 * 60)
    return total_minutes

def count_leap_years(start_year, end_year):
    count = 0
    for year in range(start_year, end_year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            count += 1
    return count

def sing_minutes(minutes):
    p = inflect.engine()
    years, minutes = divmod(minutes, 365 * 24 * 60)
    days, minutes = divmod(minutes, 24 * 60)
    hours, minutes = divmod(minutes, 60)
    result = []
    if years > 0:
        result.append(p.number_to_words(years) + " year" + ("s" if years > 1 else ""))
    if days > 0:
        result.append(p.number_to_words(days) + " day" + ("s" if days > 1 else ""))
    if hours > 0:
        result.append(p.number_to_words(hours) + " hour" + ("s" if hours > 1 else ""))
    if minutes > 0:
        result.append(p.number_to_words(minutes) + " minute" + ("s" if minutes > 1 else ""))
    return " ".join(result)

def main():
    try:
        birthdate_str = input("Please enter your date of birth in YYYY-MM-DD format: ")
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter your birthdate in YYYY-MM-DD format.")
        sys.exit(1)

    age_in_minutes = calculate_age_in_minutes(birthdate)
    if age_in_minutes < 0:
        raise ValueError("Minus %s" % sing_minutes(-age_in_minutes))
    else:
        print(sing_minutes(age_in_minutes))

if __name__ == "__main__":
    main()
