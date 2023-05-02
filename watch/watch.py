import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'src="(.*?youtube.*?)".*?</iframe>', s, re.DOTALL | re.IGNORECASE)
    if match:
        url = match.group(1)
        url = re.sub(r'^//', 'https://', url)
        return url
    else:
        return None


if __name__ == "__main__":
    main()
