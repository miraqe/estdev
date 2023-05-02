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
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(pattern, ip)
    if not match:
        return False
    parts = match.groups()
    for part in parts:
        if int(part) > 255:
            return False
    return True




if __name__ == "__main__":
    main()

