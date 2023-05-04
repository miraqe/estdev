import project

def test_add_numbers():
    assert project.add_numbers(2, 3) == 5
    assert project.add_numbers(0, 0) == 0
    assert project.add_numbers(-1, 1) == 0

def test_multiply_numbers():
    assert project.multiply_numbers(2, 3) == 6
    assert project.multiply_numbers(0, 5) == 0
    assert project.multiply_numbers(-2, -3) == 6

def test_reverse_string():
    assert project.reverse_string("hello") == "olleh"
    assert project.reverse_string("") == ""
    assert project.reverse_string("racecar") == "racecar"
