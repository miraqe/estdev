# faces.py

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("Please enter some text: ")
    output = convert(user_input)
    print(output)

if __name__ == "__main__":
    main()