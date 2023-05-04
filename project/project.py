import requests
import json
import random

def main():
    print("Hi there! My name is AnnaBot! I can help you with the following: calculation, dictionary, spell check, weather. If you wish to leave the AnnaBot, simply type exit! How can I help you today?")
    while True:
        user_input = input().lower()
        if user_input == "calculation":
            expression = input("What calculation would you like to perform?\n")
            print(calculate(expression))
        elif user_input == "dictionary":
            word = input("Please enter a word:\n").lower()
            print(dictionary(word))
        elif user_input == "spell check":
            sentence = input("Please enter a sentence:\n").lower()
            print(spell_check(sentence))
        elif user_input == "weather":
            city = input("Please enter a city:\n").lower()
            print(weather(city))
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            print("I'm sorry, I didn't understand that. Can you please type your request again? I can help you with calculation, dictionary, spell check and weather.")


def calculate(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"
    except:
        return "Invalid expression. Please try again."


def dictionary(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        return f"{word.capitalize()}: {definition}"
    else:
        return "Word not found. Please try again."



def spell_check(sentence):
    print("Please enter a sentence: ")
    sentence = input().lower()
    words = sentence.split()
    d = enchant.Dict("en_US")
    misspelled = []
    for word in words:
        if not d.check(word):
            misspelled.append(word)
    if not misspelled:
        print("No spelling errors found!")
    else:
        print("The following words are misspelled:")
        for word in misspelled:
            print(word)

def weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, API_key)
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    return "The current temperature in {} is {} degrees Celsius".format(city.title(), temperature)


def weather(city):
    print("Please enter a city: ")
    city = input().lower()
    temperature = random.randint(-10, 40)
    descriptions = ["sunny", "cloudy", "rainy", "snowy"]
    description = random.choice(descriptions)
    print(f"The current temperature in {city.capitalize()} is {temperature}°C and the weather is {description}.")



if __name__ == "__main__":
    main()
