from datetime import datetime

while True:
    date_str = input("Enter a date in the format MM/DD/YYYY or Month Day, Year: ").strip()

    try:
        datetime_obj = datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        try:
            datetime_obj = datetime.strptime(date_str, "%B %d, %Y")
        except ValueError:
            print("Invalid date format. Please try again.")
            continue
        else:
            date_str = datetime_obj.strftime("%m/%d/%Y")

    if datetime_obj.year < 1900:
        print("Date is too old. Please enter a more recent date.")
        continue

    break

print(datetime_obj.strftime("%Y-%m-%d"))
