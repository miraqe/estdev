from seasons import *

def test_calculate_age_in_minutes():
    assert calculate_age_in_minutes(date(2022, 5, 3)) == 0
    assert calculate_age_in_minutes(date(2021, 5, 3)) == 525600
    assert calculate_age_in_minutes(date(2020, 5, 3)) == 1051200

def test_main(monkeypatch):
    user_input = '2020-05-03'
    monkeypatch.setattr('builtins.input', lambda x: user_input)
    assert main() == "You are one million, fifty-one thousand, two hundred minutes old."

    user_input = '2021-05-03'
    monkeypatch.setattr('builtins.input', lambda x: user_input)
    assert main() == "You are five hundred twenty-five thousand, six hundred minutes old."

    user_input = '1990-02-30'
    monkeypatch.setattr('builtins.input', lambda x: user_input)
    assert main() == "Invalid date format. Please enter in YYYY-MM-DD format."

    user_input = '2023-05-03'
    monkeypatch.setattr('builtins.input', lambda x: user_input)
    assert main() == "You are zero minutes old."
