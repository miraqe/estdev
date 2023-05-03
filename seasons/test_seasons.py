import season

def test(season, date, minutes):
    result = subprocess.run(
        [sys.executable, "seasons.py", date], stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    if output != minutes:
        return f"{season}: expected {minutes}, but got {output}"
    return None

# set TODAY to January 1, 2000
TODAY = "2000-01-01"

# run tests
tests = [
    ["winter", "1999-01-01", "Five hundred twenty-five thousand, six hundred minutes"],
    ["spring", "2001-01-01", "One million, fifty-one thousand, two hundred minutes"],
    ["summer", "1995-01-01", "Two million, six hundred twenty-nine thousand, four hundred forty minutes"],
    ["fall", "2020-06-01", "Six million, ninety-two thousand, six hundred forty minutes"],
    ["none", "1998-06-20", "Eight hundred six thousand, four hundred minutes"]
]

failures = []
for season, date, minutes in tests:
    error = test(season, date, minutes)
    if error:
        failures.append(error)

if failures:
    print("\n".join(failures))
else:
    print("All checks pass.")
