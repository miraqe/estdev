import random

while True:
    level_str = input("Level: ")
    if not level_str.isdigit():
        continue
    level = int(level_str)
    if 1 <= level <= 100:
        break

number = random.randint(1, level)
guess = None

while guess != number:
    guess_str = input("Guess: ")
    if not guess_str.isdigit():
        print(input("Guess: "))
        continue
    guess = int(guess_str)
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
