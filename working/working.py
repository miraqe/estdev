import re

def convert(time_range: str) -> str:
    pattern = re.compile(r'(\d{1,2}):(\d{2})\s*([AP]M)')
    times = pattern.findall(time_range)
    if not times or len(times) != 2:
        return "Invalid input format"

    time_1, time_2 = times[0], times[1]
    hour_1, minute_1, period_1 = time_1
    hour_2, minute_2, period_2 = time_2

    # Convert to 24-hour format
    if period_1 == 'PM' and hour_1 != '12':
        hour_1 = str(int(hour_1) + 12)
    if period_2 == 'PM' and hour_2 != '12':
        hour_2 = str(int(hour_2) + 12)
    if period_1 == 'AM' and hour_1 == '12':
        hour_1 = '00'
    if period_2 == 'AM' and hour_2 == '12':
        hour_2 = '00'

    time_1 = f"{hour_1}:{minute_1}"
    time_2 = f"{hour_2}:{minute_2}"

    # Handle ranges that cross over midnight
    if time_1 < time_2:
        return f"{time_1} to {time_2}"
    else:
        return f"{time_1} to {time_2} + 24 hours"
