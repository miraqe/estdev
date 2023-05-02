import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe.+?src=[\'"](https?:\/\/www\.youtube\.com\/embed\/.+?)[\'"].*?<\/iframe>'
    match = re.search(pattern, s)
    if match:
        return match.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
