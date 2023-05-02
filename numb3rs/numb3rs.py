import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit(0)


def validate(ip):
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    if not re.match(pattern, ip):
        
        sys.exit(1)
    octets = ip.split('.')
    for octet in octets:
        if int(octet) > 255:
            return False
    return True



if __name__ == "__main__":
    main()
