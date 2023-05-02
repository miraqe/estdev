import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # pattern to match a valid IP address
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if re.match(pattern, ip):
        return True
    else:
        return False

if __name__ == "__main__":
    if not validate(sys.argv[1]):
        print("Invalid IPv4 address", file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)
