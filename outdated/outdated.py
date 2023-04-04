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
    date_str = input("Enter a date in the format MM/DD/YYYY or Month Day, Year: ")
    if len(date_str.split()) == 2 and date_str.split()[1].isdigit() and len(date_str.split()[1]) == 4:
        try:
            date_str = date_str.replace(",", "")
            parts = date_str.split()
            month, day, year = parts
            month_num = MONTHS.index(month) + 1
            date_str = f"{month_num:02}/{day}/{year}"
            datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please try again.")
    else:
        try:
            datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please try again.")

print(datetime_obj.strftime("%Y-%m-%d"))
