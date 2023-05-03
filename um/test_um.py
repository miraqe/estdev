from um import count

def test_empty_string():
    assert count("") == 0

def test_no_um():
    assert count("hello world") == 0

def test_one_um():
    assert count("um") == 1
    assert count("Um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_two_um():
    assert count("Um, thanks, um...") == 2
