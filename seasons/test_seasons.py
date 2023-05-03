from datetime import date, timedelta
from seasons import get_birthdate, minutes_since_birth, main



def test_minutes_since_birth():
    birthdate = date(2000, 1, 1)
    now = date.today()
    expected_minutes = ((now - birthdate).days * 24 * 60) + (now - birthdate).seconds // 60
    assert minutes_since_birth(birthdate) == expected_minutes


def test_main(capsys):
    birthdate
