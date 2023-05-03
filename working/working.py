import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid input format")
    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or "0")
    start_meridiem = match.group(3)
    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or "0")
    end_meridiem = match.group(6)
    if start_hour > 12 or start_minute >= 60 or end_hour > 12 or end_minute >= 60:
        raise ValueError("Invalid time")
    if start_meridiem == "PM" and start_hour != 12:
        start_hour += 12
    elif start_meridiem == "AM" and start_hour == 12:
        start_hour = 0
    if end_meridiem == "PM" and end_hour != 12:
        end_hour += 12
    elif end_meridiem == "AM" and end_hour == 12:
        end_hour = 0
    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()
