import emoji

emoji_dict = emoji.EMOJI_ALIAS_UNICODE

text = input("Enter a string: ")

for alias, emoji_char in emoji_dict.items():
    # Replace the alias with the corresponding emoji
    text = text.replace(alias, emoji_char)

print(text)