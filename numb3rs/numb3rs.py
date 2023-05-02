import re

def validate(ip):
    bytes = ip.split('.')
    if len(bytes) != 4:
        return False
    for byte in bytes:
        if not byte.isdigit() or int(byte) < 0 or int(byte) > 255:
            return False
    return True
