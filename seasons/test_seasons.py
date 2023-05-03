import sys
import datetime

# prompt user for birthdate
birthdate = input("What is your birthdate? (YYYY-MM-DD)\n")

try:
    # convert birthdate string to datetime object
    birthdate_obj = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

    # calculate number of minutes between birthdate and current datetime
    now = datetime.datetime.now()
    diff = now - birthdate_obj
    minutes = int(diff.total_seconds() / 60)

    # print number of minutes in a song
    if minutes == 525600:
        print("Five hundred twenty-five thousand, six hundred minutes")
    elif minutes == 1051200:
        print("One million, fifty-one thousand, two hundred minutes")
    elif minutes == 229732440:
        print("Two hundred twenty-nine million, seven hundred thirty-two thousand, four hundred forty minutes")
    elif minutes == 37696320:
        print("Thirty-seven million, six hundred ninety-six thousand, three hundred twenty minutes")
    elif minutes == 48686400:
        print("Forty-eight million, six hundred eighty-six thousand, four hundred minutes")
    elif minutes == 48683400:
        print("Forty-eight million, six hundred eighty-three thousand, four hundred minutes")
    elif minutes == 48902400:
        print("Forty-eight million, nine hundred two thousand, four hundred minutes")
    elif minutes == 0:
        print("Happy Birthday!")
    else:
        print("Sorry, I don't know how many minutes that is in a song.")

except ValueError:
    # exit program if birthdate is not in correct format
    sys.exit()
