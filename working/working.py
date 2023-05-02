from datetime import datetime
import re

def convert(time_range: str) -> str:
    pattern = re.compile(r'(\d{1,2}):(\d{2})\s*([AP]M)')
    time_1, time_2 = pattern.findall(time_range)
    time_1_hour = int(time_1[0])
    time_1_minute = int(time_1[1])
    time_1_suffix = time_1[2]
    time_2_hour = int(time_2[0])
    time_2_minute = int(time_2[1])
    time_2_suffix = time_2[2]
    print(time_1, time_2)

    if time_1_suffix == 'PM' and time_1_hour != 12:
        time_1_hour += 12
    elif time_1_suffix == 'AM' and time_1_hour == 12:
        time_1_hour = 0

    if time_2_suffix == 'PM' and time_2_hour != 12:
        time_2_hour += 12
    elif time_2_suffix == 'AM' and time_2_hour == 12:
        time_2_hour = 0

    time_1_in_minutes = time_1_hour * 60 + time_1_minute
    time_2_in_minutes = time_2_hour * 60 + time_2_minute

    if time_2_in_minutes < time_1_in_minutes:
        time_2_in_minutes += 24 * 60

    time_1_formatted = datetime.strptime(f"{time_1_hour}:{time_1_minute}", "%H:%M")
    time_2_formatted = datetime.strptime(f"{time_2_hour}:{time_2_minute}", "%H:%M")

    return f"{time_1_formatted.strftime('%H:%M')} to {time_2_formatted.strftime('%H:%M')}"


