import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit(0)


def validate(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$"
    if re.match(pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
