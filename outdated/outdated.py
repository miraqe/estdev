months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
    try:

        # user input
        date = input("Date: ").strip()

        # check if first charcter of string is not letter for (September 13, 1988)
        if not date[0].isdigit():

        # split the input string into month_day and year
            month_day, year = date.split(",")

        # split the month_day string into month and day
            month, day = month_day.split(" ")

        # if day are between 1 - 31 print the output
            if (1<= int(day) <= 31):
                print(f"{year}-{int(months.index(month)+1):02}-{int(day):02}")
                break
        else:

            # split the input string into
            month,day,year = date.split("/")

            # check if month is between 1-12 and day is between 1-31 print the output
            if (1 <= int(month) <= 12) and (1 <= int(day) <=31):
                print(f"{year}-{int(month):02}-{int(day):02}")
                break

    except:
        pass
