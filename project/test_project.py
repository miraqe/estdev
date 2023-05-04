import pytest
import requests_mock
from project import calculate, dictionary, spell_check, weather

def test_calculate(monkeypatch):
    inputs = ['1+1', '5*5', '6/0']
    expected_outputs = ['The result of 1+1 is 2', 'The result of 5*5 is 25', 'Invalid expression. Please try again.']

    for i in range(len(inputs)):
        monkeypatch.setattr('builtins.input', lambda _: inputs[i])
        assert calculate() == expected_outputs[i]

def test_dictionary_lookup(monkeypatch):
    inputs = ['cat', 'dog', 'invalid_word']
    expected_outputs = ['Cat: A small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed.\n', 'Dog: A domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, nonretractable claws, and a barking, howling, or whining voice.\n', 'Word not found. Please try again.\n']

    with requests_mock.Mocker() as m:
        for i in range(len(inputs)):
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{inputs[i]}"
            if i < 2:
                response = {"meanings":[{"definitions":[{"definition":"A small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed."}]}]}
                m.get(url, json=response)
            else:
                m.get(url, status_code=404)

            monkeypatch.setattr('builtins.input', lambda _: inputs[i])
            assert dictionary() == expected_outputs[i]

def test_spell_check(monkeypatch):
    inputs = ['I have an apple.', 'I have a appel.']
    expected_outputs = ['No spelling errors found!', 'Error at position 10: appel (suggested replacements: apple)\n']

    with requests_mock.Mocker() as m:
        for i in range(len(inputs)):
            url = "https://api.textgears.com/spelling"
            params = {'key': 'YOUR_API_KEY', 'text': inputs[i]}
            response = {"errors":[{"position":10,"length":5,"bad":"appel","better":["apple","appellate","appeal"]}]}

            m.get(url, json=response)

            monkeypatch.setattr('builtins.input', lambda _: inputs[i])
            assert spell_check() == expected_outputs[i]

def test_weather(monkeypatch):
    inputs = ['new york', 'invalid_city']
    expected_outputs = ['The current temperature in New york is', 'City not found. Please try again.']

    with requests_mock.Mocker() as m:
        for i in range(len(inputs)):
            url = f"https://api.openweathermap.org/data/2.5/weather?q={inputs[i]}&appid=YOUR_API_KEY&units=metric"
            if i == 0:
                response = {"main":{"temp":16},"weather":[{"description":"overcast clouds"}]}
                m.get(url, json=response)
            else:
                m.get(url, status_code=404)

            monkeypatch.setattr('builtins.input', lambda _: inputs[i])
            assert expected_outputs[i] in weather()
