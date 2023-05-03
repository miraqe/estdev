from datetime import date, datetime
import inflect
import sys
import re

p = inflect.engine()

class Time:
    def __init__(self, target_date):
        self.target_date  = target_date

    def __str__(self):
        # prints out the output at the end

    # operator overload
    def __sub__(self, other):
        # perform the subtraction and return the result

    @staticmethod
    def validate_date(target_date):
        # use regex to validate the proper format
        # return boolean (true if the match is found, false otherwise)

    @classmethod
    def get(cls):
        # prompt the user for input
        # validate the input by calling the static method validate_date and pass the user's input
        # if valid, pass in that user input the cls, otherwise exit using sys.exit() with an error message
        # Remember datetime.strptime allows you to turn a string into a DateTime object to make it easier for math operations

def main():
    then = Time.get()

    # gets the current date so no need to ask the user
    now = Time(date.today())
    print(now - then)

if _name_ == "__main__":
    main()

