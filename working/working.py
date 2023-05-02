import re

def to_24h(time_str):
    if time_str.endswith("AM"):
        if time_str.startswith("12"):
            hour = 0
        else:
            hour = int(time_str[:time_str.index(":")])
        minute = int(time_str[time_str.index(":")+1:time_str.index(" ")])
    elif time_str.endswith("PM"):
        if time_str.startswith("12"):
            hour = 12
        else:
            hour = int(time_str[:time_str.index(":")]) + 12
        minute = int(time_str[time_str.index(":")+1:time_str.index(" ")])
    else:
        raise ValueError("Invalid time format")

    # check if end time is before start time and add 24 hours if it is
    if "to" in time_str:
        start, end = time_str.split("to")
        end_hour = int(end[:end.index(":")])
        if end.endswith("PM") and end_hour != 12:
            end_hour += 12
        elif end.endswith("AM") and end_hour == 12:
            end_hour = 0
        if end_hour < hour:
            end_hour += 24
        end_minute = int(end[end.index(":")+1:end.index(" ")])
        return f"{hour:02d}:{minute:02d} to {end_hour:02d}:{end_minute:02d}"
    else:
        return f"{hour:02d}:{minute:02d}"

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
    return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"
