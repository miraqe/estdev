def validate(ip):
    # Split the IP address into its four bytes
    bytes = ip.split('.')

    # Check that there are exactly four bytes
    if len(bytes) != 4:
        return False

    # Check that each byte is between 0 and 255
    for byte in bytes:
        if not byte.isdigit():
            return False
        if int(byte) < 0 or int(byte) > 255:
            return False

    return True


def main():
    ip = input("IPv4 Address: ")
    if not validate(ip):
        print(f"Error: {ip} is not a valid IPv4 address")
        sys.exit(1)
    else:
        print(f"{ip} is a valid IPv4 address")
        sys.exit(0)
