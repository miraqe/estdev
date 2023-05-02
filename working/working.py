import re


def convert(s):
    # Match the input string to one of the two allowed formats
    match = re.match(r"(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)", s)
    if not match:
        raise ValueError("Invalid input format")

    # Extract the hours, minutes, and meridiem for the start and end times
    start_hour = int(match.group(1))
    start_minute = int(match.group(2)[1:]) if match.group(2) else 0
    start_meridiem = match.group(3)
    end_hour = int(match.group(4))
    end_minute = int(match.group(5)[1:]) if match.group(5) else 0
    end_meridiem = match.group(6)

    # Check that the hours and minutes are valid
    if start_hour > 12 or end_hour > 12 or start_minute >= 60 or end_minute >= 60:
        raise ValueError("Invalid time")

    # Convert the start and end times to 24-hour format
    if start_meridiem == "PM" and start_hour != 12:
        start_hour += 12
    if end_meridiem == "PM" and end_hour != 12:
        end_hour += 12
    if end_hour < start_hour or (end_hour == start_hour and end_minute < start_minute):
        end_hour += 24

    # Calculate the total number of minutes between the start and end times
    total_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)

    # Calculate the hours and minutes from the total number of minutes
    hours, minutes = divmod(total_minutes, 60)

    # Format the output string
    return f"{start_hour:02d}:{start_minute:02d} to {start_hour+hours:02d}:{minutes:02d}"
