from bank import value

def main():
    test_value()
    test_numbers()
    test_case()

def test_value():
    assert value("hello") == 0
    assert value("Hello, Anna") == 0
    assert value("What's happening") == 100
    assert value("hey") == 20
    assert value("Hi") == 20

def test_numbers():
    assert value('10') == 100
    assert value('200') == 100

def test_case():
    assert value('UPPER') == 100
    assert value('HELLO') == 0
    assert value('how are you') == 20
    assert value('welcome') == 100
    assert value('sUP dUde') == 100

if _name_ == "__main__":
    main()