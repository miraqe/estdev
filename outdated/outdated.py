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
        date_str = date_str.replace(",", "")
        parts = date_str.split()
        if len(parts) == 3:
            month, day, year = parts
            month_num = 0
            for i, m in enumerate(MONTHS):
                if m.startswith(month[:3]):
                    month_num = i + 1
                    break
            if month_num == 0:
                raise ValueError("Invalid month")
            date_str = f"{month_num:02}/{day}/{year}"
        datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")
        break
    except ValueError:
        print("Invalid date format. Please try again.")

print(datetime_obj.strftime("%Y-%m-%d"))
