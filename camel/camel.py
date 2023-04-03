def main():
    # Prompt the user for a variable name in camel case
    camel_name = input("Enter a variable name in camel case: ")

    # Convert the variable name to snake case
    snake_name = ""
    for c in camel_name:
        if c.isupper():
            snake_name += "_" + c.lower()
        else:
            snake_name += c

    # Output the variable name in snake case
    print("The variable name in snake case is:", snake_name)

if __name__ == "__main__":
    main()
