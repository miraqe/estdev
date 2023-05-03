import pytest
import seasons


def test_one_year_ago():
    assert seasons.calculate_age_in_minutes("1999-01-01") == "525600"


def test_two_years_ago():
    assert seasons.calculate_age_in_minutes("1998-01-01") == "1051200"


def test_today():
    assert seasons.calculate_age_in_minutes("2000-01-01") == "0"


def test_invalid_date():
    with pytest.raises(SystemExit):
        seasons.calculate_age_in_minutes("invalid-date-format")


def test_word_form():
    assert seasons.calculate_age_in_minutes("1999-01-01") == "five hundred twenty-five thousand six hundred"


if __name__ == "__main__":
    pytest.main()
