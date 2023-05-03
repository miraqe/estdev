from datetime import datetime
import seasons
import pytest


def test_minutes_one_year_ago():
    # Set today's date to 2001-01-01
    seasons.today = datetime(2001, 1, 1).date()
    # Calculate the date one year ago
    birth_date = datetime(2000, 1, 1).date()
    # Calculate the expected number of minutes
    expected_minutes = 525600
    # Convert expected minutes to words
    p = inflect.engine()
    expected_words = p.number_to_words(expected_minutes)
    # Call the main function and capture its output
    result = seasons.calculate_age(birth_date)
    # Convert the result to words
    result_words = p.number_to_words(result)
    # Check that the result matches the expected output
    assert result_words == expected_words


def test_minutes_two_years_ago():
    # Set today's date to 2001-01-01
    seasons.today = datetime(2001, 1, 1).date()
    # Calculate the date two years ago
    birth_date = datetime(1999, 1, 1).date()
    # Calculate the expected number of minutes
    expected_minutes = 1051200
    # Convert expected minutes to words
    p = inflect.engine()
    expected_words = p.number_to_words(expected_minutes)
    # Call the main function and capture its output
    result = seasons.calculate_age(birth_date)
    # Convert the result to words
    result_words = p.number_to_words(result)
    # Check that the result matches the expected output
    assert result_words == expected_words


def test_invalid_date_format():
    # Set today's date to 2001-01-01
    seasons.today = datetime(2001, 1, 1).date()
    # Try to calculate age with an invalid date format
    with pytest.raises(SystemExit):
        seasons.calculate_age("not a valid date")
