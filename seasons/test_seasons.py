
from seasons import check_birthday


def main():
    test_1()
    test_2()

def test_1():
    assert check_birthday(2003, 5,17) == "Ten million, one hundred fourteen thousand, five hundred sixty minutes"
    assert check_birthday(2000, 2,1) == "Eleven million, eight hundred forty-four thousand minutes"

def test_2():
    assert check_birthday(23 , 1, 2000) == "Invalid Date"

if _name_ == "__main__":
    main()