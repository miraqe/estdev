import project

def calculate(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except:
        return "Invalid expression. Please try again."

# test_project.py
def test_calculate():
    assert project.calculate("1+1") == "The result of 1+1 is 2"
    assert project.calculate("2*3") == "The result of 2*3 is 6"
    assert project.calculate("4/2") == "The result of 4/2 is 2.0"
    assert project.calculate("4//2") == "The result of 4//2 is 2"
    assert project.calculate("2**3") == "The result of 2**3 is 8"
    assert project.calculate("1.5+2.5") == "The result of 1.5+2.5 is 4.0"
    assert project.calculate("1/0") == "Invalid expression. Please try again."
