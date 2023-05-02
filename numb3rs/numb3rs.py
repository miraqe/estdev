import re

def validate(ip):
    # Use regex to check that the input is a valid IPv4 address
    regex = r'^([01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.([01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.([01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.([01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$'
    if re.search(regex, ip):
        return True
    else:
        return False
