import sys
import re

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print(f"{ip} is a valid IPv4 address.")
    else:
        print(f"{ip} is not a valid IPv4 address.")
        sys.exit(1)


def validate(ip):
    octets = ip.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        value = int(octet)
        if value < 0 or value > 255:
            return False
    return True


if __name__ == "__main__":
    main()

