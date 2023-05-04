import requests
import enchant
import json

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


def calculate(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except:
        return "Invalid expression. Please try again."


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


def weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {desc} skies."
    else:
        return "Sorry, could not get weather information for that city."


if __name__ == "__main__":
    main()
