import requests
from spellchecker import SpellChecker
from bs4 import BeautifulSoup

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
            print(spell_check(word))
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
    spell = SpellChecker()
    suggestions = spell.candidates(word)
    if suggestions:
        return f"{word.title()}: Did you mean '{spell.correction(word)}'?"
    else:
        return f"Sorry, no definition found for {word}."



from spellchecker import SpellChecker

def spell_check(sentence):
    spell = SpellChecker()
    words = sentence.split()
    checked = []
    for i, word in enumerate(words):
        if not spell.check(word):
            suggestions = spell.candidates(word)
            checked.append(f"Error at position {i}: {word} (suggested replacements: {', '.join(suggestions)})")
        else:
            checked.append(word)
    if checked == words:
        return "No spelling errors found!"
    else:
        return " ".join(checked)



def weather(city):
    url = f"https://www.timeanddate.com/weather/{city.replace(' ', '-')}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        temp = soup.find(class_='h2').get_text().split()[0]
        desc = soup.find(class_='small').get_text().strip()
        return f"The temperature in {city.title()} is {temp}°C with {desc} skies."
    else:
        return "Sorry, could not get weather information for that city."



if __name__ == "__main__":
    main()
