import sys
import datetime

def calculate_minutes(date1, date2):
    """
    Calculates the number of minutes between two dates
    """
    diff = date2 - date1
    minutes = int(round(diff.total_seconds() / 60))
    return minutes

def format_number(num):
    """
    Formats a number with commas and returns it as a string
    """
    return "{:,}".format(num)

def main():
    # get current date
    current_date = datetime.date(2000, 1, 1)

    # get input date from user
    input_date_str = input("Enter a date in the format YYYY-MM-DD: ")
    try:
        input_date = datetime.datetime.strptime(input_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
        sys.exit(1)

    # calculate the number of minutes between the two dates
    minutes = calculate_minutes(input_date, current_date)

    # format the number of minutes with commas
    formatted_minutes = format_number(minutes)

    # print the result
    print(formatted_minutes + " minutes")

if __name__ == "__main__":
    main()
