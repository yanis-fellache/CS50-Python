import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        begin, end = s.split("to")
        final_begin = start(begin)
        final_end = stop(end)
        if re.search(r"12", final_begin):
            final_begin = re.sub("12", "00", final_begin)
        if re.search(r"24", final_begin):
            final_begin = re.sub("24", "12", final_begin)
        if re.search(r"12", final_end):
            final_end = re.sub("12", "00", final_end)
        if re.search(r"24", final_end):
            final_end = re.sub("24", "12", final_end)
        return (final_begin + " to " + final_end)
    except:
        raise ValueError


def start(s):
    try:
        matches_begin = re.search(r"(\d\d?):?(\d\d)? ((?:A|P)M)", s)
        if int(matches_begin.group(1)) > 12:
            raise ValueError
        if matches_begin.group(3) == "AM":
            if matches_begin.group(2) == None:
                if len(matches_begin.group(1)) == 1:
                    final_begin = "0" + matches_begin.group(1) + ":00"
                elif len(matches_begin.group(1)) == 2:
                    final_begin = matches_begin.group(1) + ":00"
            else:
                if int(matches_begin.group(2)) >= 60:
                    raise ValueError
                if len(matches_begin.group(1)) == 1:
                    final_begin = "0" + matches_begin.group(1) + ":" + matches_begin.group(2)
                elif len(matches_begin.group(1)) == 2:
                    final_begin = matches_begin.group(1) + ":" + matches_begin.group(2)
            return final_begin
        elif matches_begin.group(3) == "PM":
            if matches_begin.group(2) == None:
                final_begin = str(int(matches_begin.group(1)) + 12) + ":00"
            else:
                final_begin = str(int(matches_begin.group(1)) + 12) + ":" + matches_begin.group(2)
            return final_begin
    except:
        raise ValueError
def stop(e):
    try:
        matches_end = re.search(r"(\d\d?):?(\d\d)? ((?:A|P)M)", e)
        if int(matches_end.group(1)) > 12:
            raise ValueError
        if matches_end.group(3) == "AM":
            if matches_end.group(2) == None:
                if len(matches_end.group(1)) == 1:
                    final_end = "0" + matches_end.group(1) + ":00"
                elif len(matches_end.group(1)) == 2:
                    final_end = matches_end.group(1) + ":00"
            else:
                if int(matches_end.group(2)) >= 60:
                    raise ValueError
                if len(matches_end.group(1)) == 1:
                    final_end = "0" + matches_end.group(1) + ":" + matches_end.group(2)
                elif len(matches_end.group(1)) == 2:
                    final_end = matches_end.group(1) + ":" + matches_end.group(2)
            return final_end
        elif matches_end.group(3) == "PM":
            if matches_end.group(2) == None:
                final_end = str(int(matches_end.group(1)) + 12) + ":00"
            else:
                final_end = str(int(matches_end.group(1)) + 12) + ":" + matches_end.group(2)
            return final_end

    except:
        raise ValueError

if __name__ == "__main__":
    main()
