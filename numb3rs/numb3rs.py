def validate(ip):
    # Split the IP address into its component bytes
    bytes = ip.split(".")

    # Check that the IP address has exactly four bytes
    if len(bytes) != 4:
        return False

    # Check that each byte is an integer between 0 and 255
    for byte in bytes:
        try:
            num = int(byte)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False

    # If we made it this far, the IP address is valid
    return True


def main():
    ip = input("IPv4 Address: ")
    if not validate(ip):
        print(f"Error: {ip} is not a valid IPv4 address")
        sys.exit(1)
    else:
        print(f"{ip} is a valid IPv4 address")
        sys.exit(0)
