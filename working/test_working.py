from working import convert


def test_valid_input_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_valid_input_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_valid_input_3():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_valid_input_4():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_invalid_input_1():
    try:
        convert("9:60 AM to 5:60 PM")
    except ValueError as e:
        assert str(e) == "Invalid time"
    else:
        assert False


def test_invalid_input_2():
    try:
        convert("9 AM - 5 PM")
    except ValueError as e:
        assert str(e) == "Invalid input format"
    else:
        assert False


def test_invalid_input_3():
    try:
        convert("09:00 AM - 17:00 PM")
    except ValueError as e:
        assert str(e) == "Invalid input format"
    else:
        assert False
