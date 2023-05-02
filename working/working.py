import re

def convert(time_range: str) -> str:
    pattern = re.compile(r'(\d{1,2}):(\d{2})\s*([AP]M)')
    time_1, time_2 = pattern.findall(time_range)

    # Check if the input time is valid
    for time in (time_1, time_2):
        hour, minute = int(time[0]), int(time[1])
        if hour > 12 or minute >= 60:
            return "Invalid input format"

    # Convert to military time
    time_1_hour, time_1_minute = int(time_1[0]), int(time_1[1])
    time_2_hour, time_2_minute = int(time_2[0]), int(time_2[1])
    time_1_military = time_1_hour + 12 if time_1[2] == 'PM' and time_1_hour != 12 else time_1_hour
    time_2_military = time_2_hour + 12 if time_2[2] == 'PM' and time_2_hour != 12 else time_2_hour

    # Convert to string
    return f"{time_1_military:02d}:{time_1_minute:02d} to {time_2_military:02d}:{time_2_minute:02d}"
