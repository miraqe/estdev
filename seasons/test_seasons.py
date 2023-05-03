import seasons

def test_check_birthday():

    assert check_birthday("1999-02-28") == ("1999", "02", "28")
    assert check_birthday("1998-12-31") == ("1998", "12", "31")
    assert check_birthday("1999-01-01") == ("1999", "01", "01")
    assert check_birthday("1995-7-3") == None
    assert check_birthday("July 3, 1996") == None


if __name__=="__main__":
    main()
