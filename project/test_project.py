import project

def test_calculate():
    assert project.calculate("2+2") == "The result of 2+2 is 4"
    assert project.calculate("5-3") == "The result of 5-3 is 2"
    assert project.calculate("10/2") == "The result of 10/2 is 5.00"
    assert project.calculate("4*6") == "The result of 4*6 is 24"
    assert project.calculate("2++2") == "Invalid expression. Please try again."
    assert project.calculate("2/0") == "Cannot divide by zero. Please try again."
    assert project.calculate("abc+def") == "Invalid expression. Please try again."

def test_random_number():
    result = project.random_number(1, 10)
    assert result >= 1 and result <= 10
    result = project.random_number(50, 100)
    assert result >= 50 and result <= 100
    result = project.random_number(-10, 0)
    assert result >= -10 and result <= 0

def test_text_manipulation():
    assert project.text_manipulation("Hello World", "uppercase") == "HELLO WORLD"
    assert project.text_manipulation("Hello World", "reverse") == "dlroW olleH"
    assert project.text_manipulation("Hello World", "count") == 11
    assert project.text_manipulation("Hello World", "unknown") == "Invalid operation. Please try again."

def test_decypher():
    assert project.decypher("uv vagreangvbany fcnpr fgngvba", 13) == "hi internet security statement"
    assert project.decypher("d qrfp lbh xabj gung'f jul abj", 13) == "q does you know that's why now"
    assert project.decypher("lbh zhfg bireqbfr gur vafgvghgr", 13) == "you must overcome the obstacles"
    assert project.decypher("lbh trg gb gur bgure fvqr!", 13) == "you get to the other side!"
