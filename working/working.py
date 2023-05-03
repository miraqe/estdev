import re
import sys

def convert_time(input_time):
    # Check if input time is valid
    pattern = r"((1[0-2]|0?[1-9]):([0-5]\d)\s*(AM|PM))|((2[0-3]|1\d|0?\d):([0-5]\d)\s*(AM|PM))"
    match = re.match(pattern, input_time)
    if not match:
        raise ValueError("Invalid time format")

    # Convert input time to military time
    time, period = input_time[:-3], input_time[-2:]
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    return f"{hour:02d}:{minute:02d}"


# Get user input
try:
    time_range = input("Enter a time range: ")
    start, end = time_range.split(" to ")
    start = convert_time(start)
    end = convert_time(end)
    print(f"{start} to {end}")
except ValueError as e:
    print(e, file=sys.stderr)
