import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(html):
    # Search for the iframe tag
    iframe_search = re.search(r'<iframe.*?</iframe>', html, re.DOTALL)
    if iframe_search:
        # Extract the iframe tag
        iframe = iframe_search.group()

        # Search for the YouTube link in the iframe tag
        youtube_search = re.search(r'src=["\'](?P<link>https?://www\.youtube\.com/embed/(?P<id>[^/]+))', iframe)
        if youtube_search:
            # Extract the YouTube link and ID
            link = youtube_search.group('link')
            return link
    return None

if __name__ == "__main__":
    main()
