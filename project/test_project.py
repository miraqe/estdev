import project

def test_calculate():
    assert project.calculate("2+2") == 4

def test_dictionary():
    assert project.dictionary("computer") == "a machine for performing calculations automatically"

def test_spell_check():
    assert project.spell_check("Thiss sentence has a spelling mistake.") == "Error at position 1: Thiss (suggested replacements: This, Kiss, Miss, Diss, His)"

def test_weather():
    assert project.weather("new york") == "The current temperature in New york is 15°C and the weather is clear sky."
