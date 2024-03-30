import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        embedded = re.search(r"(^<iframe src=\"https?://(www.)?youtube.com/embed/\w+)", s)
        link = re.sub(r"<iframe src=\"https?://(www.)?youtube.com/embed", "https://youtu.be", embedded[1])
        return link

    except:
        return None







if __name__ == "__main__":
    main()
