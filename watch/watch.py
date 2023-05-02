import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    iframe = re.findall(r'<iframe .*?</iframe>', s, re.DOTALL)
    if iframe:
        iframe = iframe[0]
        src = re.findall(r'src="(.+?)"', iframe)
        if src:
            url = src[0]
            if "youtube.com" in url:
                return url
    return None


if __name__ == "__main__":
    main()
