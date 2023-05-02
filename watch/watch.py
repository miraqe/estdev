import sys
import re

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python watch.py <url>")

    url = sys.argv[1]
    res = extract_youtube_url(url)

    if res is not None:
        print(res)

def extract_youtube_url(url):
    pattern = r'<iframe.+?src="(.+?)"'
    match = re.search(pattern, url)

    if match is not None:
        iframe_src = match.group(1)
        pattern = r'youtube\..+?/embed/(.+?)(\?|")'
        match = re.search(pattern, iframe_src)

        if match is not None:
            video_id = match.group(1)
            return f"https://youtube.com/watch?v={video_id}"

        pattern = r'youtube\.com/watch\?v=(.+?)(\&|")'
        match = re.search(pattern, iframe_src)

        if match is not None:
            video_id = match.group(1)
            return f"https://youtube.com/watch?v={video_id}"

    return None

if __name__ == "__main__":
    main()
