import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Remove all tags and their contents
    s = re.sub('<.*?>', '', s)

    # Remove leading/trailing whitespace
    s = s.strip()

    # Remove consecutive whitespace
    s = re.sub('\s+', ' ', s)

    # Return the result
    return s

if __name__ == "__main__":
    main()
