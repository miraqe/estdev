import re

pattern = r"^(0?[1-9]|1[0-2])([-\/\s])(0?[1-9]|[12]\d|3[01])\2(\d{4})$|^(January|February|March|April|May|June|July|August|September|October|November|December)\s(0?[1-9]|[12]\d|3[01]),\s(\d{4})$"

while True:
    date = input("Enter a date (month/day/year or month day, year): ")
    match = re.match(pattern, date)
    if match:
        groups = match.groups()
        if groups[0].isdigit():
            month = int(groups[0])
            day = int(groups[2])
            year = int(groups[3])
        else:
            month = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ].index(groups[4]) + 1
            day = int(groups[5])
            year = int(groups[6])
        try:
            new_date = "{:04d}-{:02d}-{:02d}".format(year, month, day)
            print(new_date)
            break
        except ValueError:
            print("Invalid date format. Please try again.")
    else:
        print("Invalid date format. Please try again.")
