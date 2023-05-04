import project

def test_calculate():
    assert project.calculate("2+2") == 4
    assert project.calculate("5-3") == 2
    assert project.calculate("6*7") == 42
    assert project.calculate("10/2") == 5
    assert project.calculate("3**3") == 27
    assert project.calculate("4%3") == 1
    assert project.calculate("a+b") == None

def test_dictionary_lookup():
    assert project.dictionary_lookup("apple") == "A fruit with red or yellow or green skin and sweet to tart crisp whitish flesh"

def test_spell_check():
    assert project.spell_check("Hello, wrld!") == "Hello, world!"
    assert project.spell_check("This is a sentence.") == "This is a sentence."

def test_temperature_conversion():
    assert project.temperature_conversion(32, "fahrenheit", "celsius") == 0.0
    assert project.temperature_conversion(0, "celsius", "fahrenheit") == 32.0
    assert project.temperature_conversion(100, "celsius", "kelvin") == 373.15

def test_weather_forecast():
    assert project.weather_forecast("New York") == "The current temperature in New York is XX°C and the weather is cloudy."
