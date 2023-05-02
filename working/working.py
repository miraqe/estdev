import re
import sys

# function to convert time from 12 hour to 24 hour format
def convert_time(time):
    if time.endswith("AM"):
        if time.startswith("12"):
            return "00" + time[2:-2]
        else:
            return time[:-2]
    else:
        if time.startswith("12"):
            return time[:-2]
        else:
            return str(int(time[:2]) + 12) + time[2:-2]

if __name__ == "__main__":
    # prompt the user for input
    time_input = input("Hours: ")
    try:
        # split the input by " to " to get the start and end times
        start, end = re.split(" to ", time_input)

        # convert start and end times to 24 hour format
        start_24h = convert_time(start)
        end_24h = convert_time(end)

        # print the start and end times in the 24 hour format
        print(start_24h + " to " + end_24h)
    except ValueError:
        # if the input is invalid, raise a ValueError
        raise ValueError
