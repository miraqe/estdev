from datetime import datetime
from seasons import check_birthday

def test_check_birthday():
    assert check_birthday(datetime(1999, 1, 1)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert check_birthday(datetime(2001, 1, 1)) == "One million, fifty-one thousand, two hundred minutes"
    assert check_birthday(datetime(1995, 1, 1)) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    assert check_birthday(datetime(2020, 6, 1)) == None
    assert check_birthday(datetime(1998, 6, 20)) == "Eight hundred six thousand, four hundred minutes"
    assert check_birthday("February 6th, 1998") == None

if __name__ == "__main__":
    test_check_birthday()
