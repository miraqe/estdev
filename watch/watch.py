import sys
import re

def main():
    html = input("HTML: ")
    url = parse(html)
    if url:
        print(url)
    else:
        print("None")

import re


def parse(s):
    # Define a regular expression pattern to match a YouTube URL in an iframe src attribute
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^\s"]+)"[^>]*>'

    # Search for the pattern in the input string
    match = re.search(pattern, s)

    # If a match is found, return the corresponding youtu.be URL
    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
