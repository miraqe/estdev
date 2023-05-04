import requests
import enchant

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
    url = f"https://www.metaweather.com/api/location/search/?query={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            woeid = data[0]["woeid"] # use the first result's woeid
            url = f"https://www.metaweather.com/api/location/{woeid}/"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temp = data["consolidated_weather"][0]["the_temp"]
                desc = data["consolidated_weather"][0]["weather_state_name"]
                return f"The temperature in {city} is {temp:.1f}°C with {desc} skies."
        return "Sorry, could not get weather information for that city."
    else:
        return "Sorry, could not get weather information for that city."



if __name__ == "__main__":
    main()
