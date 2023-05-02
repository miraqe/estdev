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
    # Regular expression pattern for IPv4 addresses
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    if not re.match(pattern, ip):
        return False

    # Split IP address into octets
    octets = ip.split('.')

    # Check if each octet is a valid integer between 0 and 255
    for octet in octets:
        if not 0 <= int(octet) <= 255:
            return False

    return True



if __name__ == "__main__":
    main()

