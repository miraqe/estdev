import seasons

def test_birthday_extraction():
    assert seasons.extract_birthday("1999-02-28") == ("1999", "02", "28")
    assert seasons.extract_birthday("1998-12-31") == ("1998", "12", "31")
    assert seasons.extract_birthday("1999-01-01") == ("1999", "01", "01")
    assert seasons.extract_birthday("1995-7-3") is None
    assert seasons.extract_birthday("July 3, 1996") is None



def test_invalid_date_format():
    try:
        seasons.minutes_since_birth("February 6th, 1998")
    except SystemExit as e:
        assert e.code == "Invalid date format. Please enter in YYYY-MM-DD format."

def test_exit_code():
    assert seasons.run() == 0
