import requests
import json

def main():
    print("Hi there! My name is AnnaBot! I can help you with the following: calculation, dictionary, spell check, weather. If you wish to leave the AnnaBot, simply type exit! How can I help you today?")
    while True:
        user_input = input().lower()
        if user_input == "calculation":
            calculate()
        elif user_input == "dictionary":
            dictionary()
        elif user_input == "spell check":
            spell_check()
        elif user_input == "weather":
            weather()
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            print("I'm sorry, I didn't understand that. Can you please type your request again? I can help you with calculation, dictionary, spell check and weather.")

def calculate():
    print("What calculation would you like to perform?")
    expression = input()
    try:
        result = eval(expression)
        print(f"The answer for {expression} is {result}")
    except:
        print("Invalid expression. Please try again.")

def dictionary():
    print("Please enter a word: ")
    word = input().lower()
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        print(f"{word.capitalize()}: {definition}")
    else:
        print("Word not found. Please try again.")

def spell_check():
    print("Please enter a sentence:")
    sentence = input().lower()
    url = f"https://api.textgears.com/spelling?key=YOUR_API_KEY&text={sentence}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        errors = data['errors']
        if len(errors) == 0:
            print("No spelling errors found!")
        else:
            for error in errors:
                print(f"Error at position {error['position']}: {error['bad']} (suggested replacements: {', '.join(error['better'])})")
    else:
        print("Something went wrong. Please try again later.")

def weather():
    print("Please enter a city:")
    city = input().lower()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"The current temperature in {city.capitalize()} is {temperature}°C and the weather is {description}.")
    else:
        print("City not found. Please try again.")

if __name__ == "__main__":
    main()
