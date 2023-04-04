import datetime

# List of month names in order
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
        # Prompt the user for a date in month-day-year format
        date_str = input("Enter a date in month-day-year format (e.g., 9/8/1636): ")
        # Try to parse the date using strptime
        date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        try:
            # If parsing fails, try to parse the date in month name-day-year format
            month_name, day_str, year_str = date_str.split()
            month_num = MONTHS.index(month_name) + 1
            date_obj = datetime.datetime.strptime(f"{month_num}/{day_str}/{year_str}", "%m/%d/%Y")
        except (ValueError, IndexError):
            # If parsing fails again, prompt the user again
            print("Invalid date format. Please try again.")
            continue
    # Format the date in year-month-day format and print it
    print(date_obj.strftime("%Y-%m-%d"))
    break
