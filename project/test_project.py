import project

def test_add_numbers():
    assert project.add_numbers(2, 3) == 5
    assert project.add_numbers(-2, 3) == 5
    assert project.add_numbers(2, -3) == 5
    assert project.add_numbers(-2, -3) == 1

def test_multiply_numbers():
    assert project.multiply_numbers(2, 3) == 6
    assert project.multiply_numbers(-2, 3) == -6
    assert project.multiply_numbers(2, -3) == -6
    assert project.multiply_numbers(-2, -3) == 6

def test_reverse_string():
    assert project.reverse_string("hello world") == "dlrow olleh"
    assert project.reverse_string("") == ""
    assert project.reverse_string("racecar") == "racecar"
    assert project.reverse_string("The quick brown fox") == "xof nworb kciuq ehT"
