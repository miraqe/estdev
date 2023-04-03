# Prompt the user for a string of text
text = input("Enter a string of text: ")

# Remove all vowels from the text (both uppercase and lowercase)
vowels = "AEIOUaeiou"
text_without_vowels = ""
for char in text:
    if char not in vowels:
        text_without_vowels += char

# Output the resulting text
print(text_without_vowels)