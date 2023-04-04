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
        date_str = input("Enter a date in the format MM/DD/YYYY or Month Day, Year: ")
        date_str = date_str.strip()
        parts = date_str.split("/")
        if len(parts) == 1:
            parts = date_str.split()
            if len(parts) != 3:
                raise ValueError
            month, day, year = parts
            month_num = MONTHS.index(month) + 1
            date_str = f"{month_num:02}/{day}/{year}"
        elif len(parts) != 3:
            raise ValueError
        datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")
        break
    except (ValueError, IndexError):
        print("Invalid date format. Please try again.")

print(datetime_obj.strftime("%Y-%m-%d"))
