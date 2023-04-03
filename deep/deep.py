def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip()
    if answer.lower() == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
