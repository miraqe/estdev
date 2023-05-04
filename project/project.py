import random

def calculate(expression):
    try:
        result = eval(expression)
        if isinstance(result, float):
            if result.is_integer():
                return f"The result of {expression} is {int(result)}"
            else:
                return f"The result of {expression} is {result:.2f}"
        else:
            return f"The result of {expression} is {result}"
    except SyntaxError:
        return "Invalid expression. Please try again."
    except ZeroDivisionError:
        return "Cannot divide by zero. Please try again."
    except:
        return "An error occurred. Please try again."


def random_number(start, end):
    return f"Your random number between {start} and {end} is: {random.randint(start, end)}"

def text_manipulation(text, operation):
    if operation == "uppercase":
        return text.upper()
    elif operation == "lowercase":
        return text.lower()
    elif operation == "reverse":
        return text[::-1]
    else:
        return "Invalid operation. Please try again."

def decypher(ciphertext, key):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - key
            if shifted < ord('a'):
                shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted

def main():
    print("Hi there! My name is AnnaBot! I can help you with the following: calculation, random number, text manipulation, decypher, dictionary, spell check, weather. If you wish to leave the AnnaBot, simply type exit! How can I help you today?")
    while True:
        user_input = input().lower()
        if user_input == "calculation":
            expression = input("What calculation would you like to perform?\n")
            print(calculate(expression))
        elif user_input == "random number":
            start = int(input("Please enter the starting number:\n"))
            end = int(input("Please enter the ending number:\n"))
            print(random_number(start, end))
        elif user_input == "text manipulation":
            text = input("Please enter some text:\n")
            operation = input("What operation would you like to perform? (uppercase, lowercase, reverse)\n")
            print(text_manipulation(text, operation))
        elif user_input == "decypher":
            ciphertext = input("Please enter the ciphertext:\n")
            key = int(input("Please enter the key:\n"))
            print(decypher(ciphertext, key))
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
            print("I'm sorry, I didn't understand that. Can you please type your request again? I can help you with calculation, random number, text manipulation, decypher, dictionary, spell check and weather.")
