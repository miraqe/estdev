
from seasons import check_birthday

def main():
    test_birth_date()

def test_check_birthday():
    assert check_birthday("1998-06-02") == ("1998", "06", "02")

    assert check_birthday("1998-01-01") == ("1998", "01", "01")
    assert check_birthday("2000, 2, 29") == None
    assert check_birthday("August, 6, 20") == None




if __name__ == "__main__":
    main()