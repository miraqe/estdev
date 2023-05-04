import requests
import json

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
    url = f"https://api.textgears.com/spelling?key=YOUR_API_KEY&text={sentence}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        errors = data['errors']
        if len(errors) == 0:
            return "No spelling errors found!"
        else:
            error_messages = []
            for error in errors:
                error_messages.append(f"Error at position {error['position']}: {error['bad']} (suggested replacements: {', '.join(error['better'])})")
            return "\n".join(error_messages)
    else:
        return "Something went wrong. Please try again later."


def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return f"The current temperature in {city.capitalize()} is {temperature}°C and the weather is {description}."
    else:
        return "City not found. Please try again."


if __name__ == "__main__":
    main()
