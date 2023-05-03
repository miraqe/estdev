
from datetime import date
from seasons import calculate_age_in_minutes, sing_minutes

def test_calculate_age_in_minutes():
    birthdate = date(2000, 1, 1)
    assert calculate_age_in_minutes(birthdate) == 525600

    birthdate = date(1998, 1, 1)
    assert calculate_age_in_minutes(birthdate) == 1051200

    birthdate = date(2000, 2, 29)
    assert calculate_age_in_minutes(birthdate) == 525600

def test_sing_minutes():
    assert sing_minutes(525600) == "one year"
    assert sing_minutes(1051200) == "two years"
    assert sing_minutes(525600 * 2 + 1440) == "two years one day one minute"
    assert sing_minutes(60) == "one minute"
    assert sing_minutes(120) == "two minutes"
    assert sing_minutes(1440) == "one day
