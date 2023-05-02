import re


def convert(time_str):
    # Split the time string into start and end times
    start, end = time_str.split(" to ")

    # Convert the start time to military time
    start_hour, start_min = map(int, start[:-3].split(":"))
    start_meridian = start[-2:]
    if start_meridian == "PM" and start_hour != 12:
        start_hour += 12

    # Convert the end time to military time
    end_hour, end_min = map(int, end[:-3].split(":"))
    end_meridian = end[-2:]
    if end_meridian == "PM" and end_hour != 12:
        end_hour += 12
    if end_meridian == "AM" and end_hour == 12:
        end_hour = 0

    # Adjust the end time if it's on the next day
    if end_hour < start_hour:
        end_hour += 24

    # Format the start and end times in military format
    start_time = f"{start_hour:02d}:{start_min:02d}"
    end_time = f"{end_hour:02d}:{end_min:02d}"

    # Combine the start and end times into a string
    return f"{start_time} to {end_time}"

