import sys
import re


def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        sys.exit(0)  # success
    else:
        sys.exit(1)  # failure


def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)
    if match is None:
        return False

    # Ensure that each octet is between 0 and 255.
    octets = [int(octet) for octet in match.groups()]
    if any(octet < 0 or octet > 255 for octet in octets):
        return False

    return True


if __name__ == "__main__":
    main()
