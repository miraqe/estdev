from datetime import date
import inflect
import sys

def minutes_since_birth(birthday):
    today = date.today()
    days_since_birth = (today - birthday).days
    minutes_since_birth = days_since_birth * 24 * 60
    leap_years = count_leap_years(birthday, today)
    minutes_since_birth += leap_years * 24 * 60
    return round(minutes_since_birth)

def count_leap_years(start_date, end_date):
    leap_years = 0
    for year in range(start_date.year, end_date.year+1):
        if is_leap_year(year):
            if year == start_date.year:
                if start_date.month < 3:
                    leap_years += 1
            elif year == end_date.year:
                if end_date.month >= 3:
                    leap_years += 1
            else:
                leap_years += 1
    return leap_years

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def format_minutes(minutes):
    p = inflect.engine()
    words = []
    millions = minutes // (10**6)
    if millions > 0:
        words.append(p.number_to_words(millions))
        words.append('million')
        minutes -= millions * 10**6
    thousands = minutes // 1000
    if thousands > 0:
        words.append(p.number_to_words(thousands))
        words.append('thousand')
        minutes -= thousands * 1000
    if minutes > 0:
        words.append(p.number_to_words(minutes))
    words.append('minutes')
    return ' '.join(words)

def main():
    try:
        input_date = input('Enter your birthdate (YYYY-MM-DD): ')
        birthday = date.fromisoformat(input_date)
    except ValueError:
        sys.exit()
    minutes = minutes_since_birth(birthday)
    print(format_minutes(minutes))

if __name__ == '__main__':
    main()
