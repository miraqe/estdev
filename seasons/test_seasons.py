import seasons

def test_minutes_since_birth():
    assert seasons.minutes_since_birth("2022-05-03") == "zero minutes"
    assert seasons.minutes_since_birth("2021-05-03") == "five hundred twenty-five thousand six hundred minutes"
    assert seasons.minutes_since_birth("2020-05-03") == "one million fifty-one thousand two hundred minutes"
    assert seasons.minutes_since_birth("2000-02-29") == "eleven million five hundred fifty-eight thousand four hundred minutes"
    assert seasons.minutes_since_birth("1999-02-28") == "eleven million six hundred twenty-eight thousand minutes"
    assert seasons.minutes_since_birth("1998-12-31") == "eleven million seven hundred six thousand two hundred forty minutes"

def test_invalid_date_format():
    try:
        seasons.minutes_since_birth("2022/05/03")
    except SystemExit as e:
        assert e.code == "Invalid date format. Please enter in YYYY-MM-DD format."
