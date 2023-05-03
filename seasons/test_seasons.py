
from seasons import check_birthday

def test_check_birthday():
    assert check_birthday("525600") == "Five hundred twenty-five thousand, six hundred minutes"
    assert check birthday("1051200") == "One million, fifty-one thousand, two hundred minutes"

if __name__ == "__main__":
    main()