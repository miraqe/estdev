from working import convert

def test_valid_input_1():
    assert convert("2:30 PM to 11:45 PM") == "14:30 to 23:45"


def test_valid_input_2():
    assert convert("6:20 AM to 12:40 PM") == "06:20 to 12:40"


def test_valid_input_3():
    assert convert("10:00 PM to 8:00 AM") == "22:00 to 08:00"


def test_valid_input_4():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


def test_invalid_input_1():
    assert convert("10:00 PM to 25:00 PM") == "Invalid input format"


def test_invalid_input_2():
    assert convert("not enough values to unpack (expected 2, got 1)") == "Invalid input format"


def test_invalid_input_3():
    assert convert("10:00 PM to 12:00") == "Invalid input format"



