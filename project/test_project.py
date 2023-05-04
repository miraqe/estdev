import project

def test_calculate():
    assert project.calculate("1+1") == "The result of 1+1 is 2"
    assert project.calculate("2*3") == "The result of 2*3 is 6"
    assert project.calculate("4/2") == "The result of 4/2 is 2.0"
    assert project.calculate("4//2") == "The result of 4//2 is 2"
    assert project.calculate("2**3") == "The result of 2**3 is 8"
    assert project.calculate("1.5+2.5") == "The result of 1.5+2.5 is 4.0"
    assert project.calculate("1/0") == "Invalid expression. Please try again."

def test_dictionary():
    assert project.dictionary("apple") == "Apple: The usually round, red or yellow, edible fruit of a small tree, Malus sylvestris, of the rose family."
    assert project.dictionary("wordnotfound") == "Word not found. Please try again."

def test_spell_check():
    assert project.spell_check("Thi is a testt sentence.") == "Error at position 0: Thi (suggested replacements: The)"
    assert project.spell_check("This is another sentence.") == "No spelling errors found!"

def test_weather():
    assert project.weather("london") == "The current temperature in London is"
    assert project.weather("notacity") == "City not found. Please try again."
