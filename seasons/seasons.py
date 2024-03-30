from datetime import date
import sys
import inflect
import re

p = inflect.engine()


def main():
    try:
        print(convert(input("Date of Birth: ")))
    except:
        sys.exit("Invalid Date")

def convert(dob_input):
    dob = str_to_date(dob_input)
    time_words = p.number_to_words(int(str(date.today() - dob).split(" ")[0]) * 24 * 60)
    time_words = time_words.replace("and ", "")
    return f"{time_words.capitalize()} minutes"

def str_to_date(dob_input):
    year, month, day = dob_input.split("-")
    return date(int(year), int(month), int(day))

if __name__ == "__main__":
    main()
