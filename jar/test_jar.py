from jar import Jar

def test_init():
    # Test initializing jar with default capacity
    jar = Jar()
    assert jar.capacity == 12

    # Test initializing jar with custom capacity
    jar = Jar(20)
    assert jar.capacity == 20

    # Test initializing jar with negative capacity
    try:
        jar = Jar(-5)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test initializing jar with non-integer capacity
    try:
        jar = Jar("twelve")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

def test_str():
    # Test string representation of jar with no cookies
    jar = Jar()
    assert str(jar) == ""

    # Test string representation of jar with cookies
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    # Test depositing valid number of cookies
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    # Test depositing more cookies than capacity
    try:
        jar.deposit(5)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test depositing negative number of cookies
    try:
        jar.deposit(-2)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test depositing non-integer number of cookies
    try:
        jar.deposit("three")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

def test_withdraw():
    # Test withdrawing valid number of cookies
    jar = Jar(5)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1

    # Test withdrawing more cookies than available
    try:
        jar.withdraw(2)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test withdrawing negative number of cookies
    try:
        jar.withdraw(-1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"

    # Test withdrawing non-integer number of cookies
    try:
        jar
