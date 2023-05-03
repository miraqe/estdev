import seasons

def main():

    assert seasons.minutes_since_birth("1999-02-28") == "Eleven million, six hundred twenty-eight thousand minutes"
    assert seasons.minutes_since_birth("1998-12-31") == "Eleven million, seven hundred six thousand, two hundred forty minutes"
    assert seasons.minutes_since_birth("1999-01-01") == "Five hundred twenty-five thousand, six hundred minutes"
    assert seasons.minutes_since_birth("1995-01-01") == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    assert seasons.minutes_since_birth("1998-06-20") == "Eight hundred six thousand, four hundred minutes"


def test_invalid_date_format():
    try:
        seasons.minutes_since_birth("February 6th, 1998")
    except SystemExit as e:
        assert e.code == "Invalid date format. Please enter in YYYY-MM-DD format."

def test_exit_code():
    assert seasons.run() == 0
