import re


def convert(time_string):
    # Split the time string into start and end times
    start_time, end_time = time_string.split(' to ')

    # Convert the start time to military time
    start_time = convert_to_military(start_time)

    # If the end time is smaller than the start time, add 24 hours
    if convert_to_military(end_time) < start_time:
        end_time = add_24_hours(end_time)

    # Convert the end time to military time
    end_time = convert_to_military(end_time)

    # Convert the times to the correct format
    start_time = format_time(start_time)
    end_time = format_time(end_time)

    # Combine the times into a string and return it
    return f'{start_time} to {end_time}'

def convert_to_military(time_string):
    # Convert the time string to military time
    time_obj = datetime.strptime(time_string, '%I:%M %p')
    return time_obj.hour * 100 + time_obj.minute

def add_24_hours(time_string):
    # Add 24 hours to the time string
    time_obj = datetime.strptime(time_string, '%I:%M %p')
    time_obj += timedelta(hours=24)
    return time_obj.strftime('%I:%M %p')

def format_time(time_value):
    # Format the time value as a string
    return datetime.strptime(str(time_value), '%H%M').strftime('%I:%M %p').lstrip('0')


