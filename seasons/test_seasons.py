from datetime import datetime
from seasons import minutes_since_birth

def test_minutes_since_birth():
    assert minutes_since_birth(datetime(1999, 1, 1)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_since_birth(datetime(2001, 1, 1)) == "One million, fifty-one thousand, two hundred minutes"
    assert cminutes_since_birth(datetime(1995, 1, 1)) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"

    assert minutes_since_birth(datetime(1998, 6, 20)) == "Eight hundred six thousand, four hundred minutes"
    assert minutes_since_birth("February 6th, 1998") == None

if __name__ == "__main__":
    test_minutes_since_birth()
