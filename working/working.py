def convert(start_time, end_time):
    """
    This function takes the start time and end time in the format of "HH:MM" and returns a formatted string
    representing the working hours of an employee.
    """
    # Convert start and end time to minutes
    start_minutes = int(start_time[:2]) * 60 + int(start_time[3:])
    end_minutes = int(end_time[:2]) * 60 + int(end_time[3:])

    # Check if end time is before start time and add 24 hours to end time if it is
    if end_minutes < start_minutes:
        end_minutes += 24 * 60

    # Calculate total minutes worked
    total_minutes = end_minutes - start_minutes

    # Convert total minutes worked to hours and minutes
    hours = total_minutes // 60
    minutes = total_minutes % 60

    # Format output string
    if hours < 10:
        hours_str = "0" + str(hours)
    else:
        hours_str = str(hours)

    if minutes < 10:
        minutes_str = "0" + str(minutes)
    else:
        minutes_str = str(minutes)

    return hours_str + ":" + minutes_str + " hours worked"

if __name__ == "__main__":
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    print(working_hours(start_time, end_time))
