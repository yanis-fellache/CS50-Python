import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if length_size(matches):
        return True
    else:
        return False


def length_size(matches):
    try:
        matches.group(5)
    except:
        pass
    else:
        return False
    try:
        if int(matches.group(1)) < 0 or int(matches.group(1)) > 255:
            return False
        elif int(matches.group(2)) < 0 or int(matches.group(2)) > 255:
            return False
        elif int(matches.group(3)) < 0 or int(matches.group(3)) > 255:
            return False
        elif int(matches.group(4)) < 0 or int(matches.group(4)) > 255:
            return False
        else:
            return True
    except:
        return False


if __name__ == "__main__":
    main()
