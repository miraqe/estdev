import seasons

def main():
    birthday()

    assert main("1999-02-28") == ("1999", "02", "28")
    assert main("1998-12-31") == ("1998", "12", "31")
    assert main("1999-01-01") == ("1999", "01", "01")
    assert main("1995-7-3") == None
    assert main("July 3, 1996") == None


if __name__=="__main__":
    main()
