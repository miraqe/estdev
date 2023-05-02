import sys
import re


def main():
    print(parse(sys.stdin.read()))


def parse(s):
    # Extract all HTML tags
    tags = re.findall(r"<.*?>", s)

    # Extract tag names and attributes
    results = []
    for tag in tags:
        # Get tag name
        tag_match = re.search(r"<(\w+)", tag)
        tag_name = tag_match.group(1) if tag_match else ""

        # Get attributes
        attrs = {}
        attr_matches = re.findall(r"(\w+)\s*=\s*[\"']?([^\"']*)[\"']?", tag)
        for attr_match in attr_matches:
            attr_name, attr_value = attr_match
            attrs[attr_name] = attr_value

        results.append((tag_name, attrs))

    return results


if __name__ == "__main__":
    main()
