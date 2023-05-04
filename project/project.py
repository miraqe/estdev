import requests
import json
import random

if __name__ == '__main__':
    api_key = input("Please enter your OpenWeatherMap API key: ")

    while True:
        print("Please choose an option:")
        print("1. Dictionary")
        print("2. Spell Check")
        print("3. Weather")
        print("4. Exit")
        choice = input()

        if choice == "1":
            word = input("Please enter a word: ")
            print(dictionary(word))
        elif choice == "2":
            sentence = input("Please enter a sentence: ")
            print(spell_check(sentence))
        elif choice == "3":
            city = input("Please enter a city: ")
            print(weather(city, api_key))
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def dictionary(word):
    d = enchant.Dict("en_US")
    if d.check(word):
        definition = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()[0]['meanings'][0]['definitions'][0]['definition']
        return f"{word.capitalize()}: {definition}"
    else:
        return "The word does not exist in the English language."

def spell_check(sentence):
    d = enchant.Dict("en_US")
    words = sentence.split()
    for i in range(len(words)):
        if not d.check(words[i]):
            suggestions = d.suggest(words[i])
            return f"Error at position {i}: {words[i]} (suggested replacements: {', '.join(suggestions)})"
    return "No errors found."

def weather(city, api_key):
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        return f"The current temperature in {city.capitalize()} is {temp:.1f}°F."
    elif response.status_code == 404:
        return "City not found."
    else:
        return "Unable to retrieve weather information."


def weather(city):
    print("Please enter a city: ")
    city = input().lower()
    temperature = random.randint(-10, 40)
    descriptions = ["sunny", "cloudy", "rainy", "snowy"]
    description = random.choice(descriptions)
    print(f"The current temperature in {city.capitalize()} is {temperature}°C and the weather is {description}.")



if __name__ == "__main__":
    main()
