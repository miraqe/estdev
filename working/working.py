import re

def convert(time_range: str) -> str:
    pattern = re.compile(r'(\d{1,2}):(\d{2})\s*([AP]M)')
    matches = pattern.findall(time_range)

    if len(matches) != 2:
        raise ValueError("Invalid input format")

    time_1 = matches[0]
    time_2 = matches[1]

    time_1_hour = int(time_1[0])
    time_1_minute = int(time_1[1])
    time_1_ampm = time_1[2]

    time_2_hour = int(time_2[0])
    time_2_minute = int(time_2[1])
    time_2_ampm = time_2[2]

    if time_1_ampm == 'PM' and time_1_hour != 12:
        time_1_hour += 12
    elif time_1_ampm == 'AM' and time_1_hour == 12:
        time_1_hour = 0

    if time_2_ampm == 'PM' and time_2_hour != 12:
        time_2_hour += 12
    elif time_2_ampm == 'AM' and time_2_hour == 12:
        time_2_hour = 0

    time_1_str = f"{time_1_hour:02d}:{time_1_minute:02d}"
    time_2_str = f"{time_2_hour:02d}:{time_2_minute:02d}"

    return f"{time_1_str} to {time_2_str}"
