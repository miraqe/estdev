from numb3rs import validate

def test_valid_ipv4():
    assert validate("127.0.0.1") == True
    assert validate("192.168.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True

def test_invalid_ipv4():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("256.256.256.256") == False
    assert validate("192.168.1") == False
