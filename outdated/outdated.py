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

        # Check if input string contains a comma
        if ',' not in date_str:
            # Check if input string matches MM/DD/YYYY format
            datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")
        else:
            # Split the input string into month, day, and year
            date_parts = date_str.split()
            if len(date_parts) != 3:
                raise ValueError("Invalid date format")
            month, day, year = date_parts

            # Check if month is valid
            if month not in MONTHS:
                raise ValueError("Invalid month")
            month_num = MONTHS.index(month) + 1

            # Check if day and year are integers
            day = int(day)
            year = int(year)

            # Check if day and year are within valid ranges
            if day < 1 or day > 31:
                raise ValueError("Invalid day")
            if year < 1 or year > datetime.now().year:
                raise ValueError("Invalid year")

            # Construct the date string in MM/DD/YYYY format
            date_str = f"{month_num:02}/{day:02}/{year:04}"

            # Create a datetime object from the date string
            datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")

        break

    except ValueError as e:
        print(f"Invalid date format: {e}")
        continue

print(datetime_obj.strftime("%Y-%m-%d"))
