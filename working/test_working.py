
import re

def exists():
    """working.py and test_working.py exist"""
    check50.exists("working.py")
    check50.exists("test_working.py")


def imports():
    """working.py imports libraries other than sys and re"""
    with open("working.py") as f:
        if re.search(r"import\s+[^s]", f.read()):
            raise check50.Failure("working.py should not import any libraries other than sys and re")


def converts_9am_to_5pm():
    """working.py converts "9 AM to 5 PM" to "09:00 to 17:00" """
    check_converted_time("9 AM to 5 PM", "09:00 to 17:00")


def converts_9am_to_5pm_with_zeroes():
    """working.py converts "9:00 AM to 5:00 PM" to "09:00 to 17:00" """
    check_converted_time("9:00 AM to 5:00 PM", "09:00 to 17:00")

def converts_8pm_to_8am():
    """working.py converts "8 PM to 8 AM" to "20:00 to 08:00" """
    check_converted_time("8 PM to 8 AM", "20:00 to 08:00")

def converts_8pm_to_8am_with_zeroes():
    """working.py converts "8:00 PM to 8:00 AM" to "20:00 to 08:00" """
    check_converted_time("8:00 PM to 8:00 AM", "20:00 to 08:00")

def converts_12am_to_12pm():
    """working.py converts "12 AM to 12 PM" to "
