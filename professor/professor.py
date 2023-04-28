import random


def main():
    level = get_level()
    if level == None:
        return
    score = 0
    for i in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        num_tries = 0
        while True:
            user_answer = input(f"{x} + {y} = ")
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    print("Correct!")
                    break
                else:
                    num_tries += 1
                    if num_tries >= 3:
                        print(f"Answer: {correct_answer}")
                        break
                    else:
                        print("EEE")
            except ValueError:
                print("EEE")
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level in ("1", "2", "3"):
            return int(level)
        elif level == "0" or level == "4":
            print("EEE")
        else:
            print("EEE")


def generate_integer(level):
    if level == 1:
        digits = 1
    elif level == 2:
        digits = 2
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        return x, y
    elif level == 3:
        digits = 3
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        return x, y
    else:
        raise ValueError("EEE")
    x = random.randint(0, 10 ** digits - 1)
    y = random.randint(0, 10 ** digits - 1)
    return x, y


if __name__ == "__main__":
    main()
