import project

def test_calculate():
    assert project.calculate("1+1") == 2

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-2, 3) == 1
    assert addition(0, 0) == 0

def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(3, 5) == -2
    assert subtraction(0, 0) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 5) == 0

def test_division():
    assert division(10, 5) == 2
    assert division(-10, 5) == -2
    assert division(0, 5) == 0
    assert division(5, 0) == None

def test_dictionary_lookup():
    assert dictionary_lookup('python') == 'a high-level general-purpose programming language.'
    assert dictionary_lookup('algorithm') == 'a process or set of rules to be followed in calculations or other problem-solving operations.'
    assert dictionary_lookup('notaword') == None

def test_spell_check():
    assert spell_check('speling') == 'spelling'
    assert spell_check('definately') == 'definitely'
    assert spell_check('test') == None

def test_temperature_conversion():
    assert temperature_conversion(0, 'celsius', 'fahrenheit') == 32.0
    assert temperature_conversion(100, 'celsius', 'fahrenheit') == 212.0
    assert temperature_conversion(32, 'fahrenheit', 'celsius') == 0.0

def test_weather_forecast():
    assert weather('New York'), str)
    assert weather('Chicago'), str)
    assert weather('notacity'), type(None))
