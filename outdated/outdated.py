from datetime import datetime

MONTHS = [
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
]

while True:
    try:
        date_str = input("Enter a date in the format MM/DD/YYYY or Month Day, Year: ").strip()
        date_str = date_str.replace(",", "")
        parts = date_str.split()

        # Case when user input is Month Day, Year format
        if len(parts) == 3:
            month, day, year = parts
            if month not in MONTHS:
                raise ValueError("Invalid date format")
            year = int(year)
            if year < 1000:
                raise ValueError("Invalid date format")
            month_num = MONTHS.index(month) + 1
            date_str = f"{month_num:02}/{day}/{year}"

        # Case when user input is MM/DD/YYYY format
        datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")
        break

    except ValueError:
        print("Invalid date format. Please try again.")
        continue

print(datetime_obj.strftime("%Y-%m-%d"))
