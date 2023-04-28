from plates import is_vanity_plate

def main():
    test_start()
    test_length()
    test_numbers()
    test_zero()
    test_punc()

def test_start():
    assert is_vanity_plate('ABCDEF') == True
    assert is_vanity_plate('1ABCDE') == False
    assert is_vanity_plate('A3CDEF') == False
    assert is_vanity_plate('63CDEF') == False

def test_length():
    assert is_vanity_plate('ABCDEF') == True
    assert is_vanity_plate('ABCDE') == True
    assert is_vanity_plate('ABC') == True
    assert is_vanity_plate('AB') == True
    assert is_vanity_plate('A') == False

def test_numbers():
    assert is_vanity_plate('ABC123') == True
    assert is_vanity_plate('ABCD12') == True
    assert is_vanity_plate('ABCDE1') == True
    assert is_vanity_plate('AB23EF') == False
    assert is_vanity_plate('ABC23F') == False
    assert is_vanity_plate("AA") == True
    assert is_vanity_plate("A2") == False
    assert is_vanity_plate("2A") == False
    assert is_vanity_plate("22") == False
    assert is_vanity_plate(" 2") == False

def test_zero():
    assert is_vanity_plate('ABC102') == True
    assert is_vanity_plate('CS50') == True
    assert is_vanity_plate('ABC012') == False
    assert is_vanity_plate('ABCD01') == False

def test_punc():
    assert is_vanity_plate('ABC,23') == False
    assert is_vanity_plate('ABC 23') == False
    assert is_vanity_plate('ABC.12') == False
    assert is_vanity_plate('AB:12') == False
    assert is_vanity_plate('AB/45') == False

if _name_ == "__main__":
    main()