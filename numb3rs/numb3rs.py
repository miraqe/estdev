import re
import sys


def main():
    if validate(input("IPv4 Address: ")):
        print("True")
    else:
        print("False")
        sys.exit(1)


def validate(ip):
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    if not re.match(pattern, ip):
        return "False"

    octets = ip.split('.')
    for octet in octets:
        if int(octet) > 255:
            return "False"
    return "True"


if __name__ == "__main__":
    main()
