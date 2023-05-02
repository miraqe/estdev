import re
from datetime import datetime, timedelta

def convert(time_range: str) -> str:
    pattern = re.compile(r'(\d{1,2}):(\d{2})\s*([AP]M)')
    matches = pattern.findall(time_range)

    if len(matches) != 2:
        raise ValueError("Invalid input format")

    time_1, time_2 = matches

    time_1 = datetime.strptime(time_1[0] + ':' + time_1[1] + ' ' + time_1[2], '%I:%M %p')
    time_2 = datetime.strptime(time_2[0] + ':' + time_2[1] + ' ' + time_2[2], '%I:%M %p')

    if time_2 < time_1:
        time_2 += timedelta(days=1)

    time_diff = time_2 - time_1
    return time_1.strftime('%H:%M') + ' to ' + (time_1 + time_diff).strftime('%H:%M')
