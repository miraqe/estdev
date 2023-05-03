from datetime import datetime
from seasons import check_birthday

def test_check_birthday():
    assert check_birthday(datetime(1999, 1, 1)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert check_birthday(datetime(2001, 1, 1)) == "Minus five hundred twenty-six thousand, four hundred sixty minutes"
    assert check_birthday(datetime(1995, 1, 1)) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    assert check_birthday(datetime(2020, 6, 1)) == "Minus ten million, six hundred twenty thousand, eight hundred sixty minutes"
    assert check_birthday(datetime(1998, 6, 20)) == "Eight hundred six thousand, four hundred minutes"

if __name__ == "__main__":
    test_check_birthday()
