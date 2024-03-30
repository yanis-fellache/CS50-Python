import sys

try:
    lines = 0
    if len(sys.argv) < 2:
        raise IndexError
    elif len(sys.argv) > 2:
        raise Exception
    elif not sys.argv[1].endswith(".py"):
        raise FileNotFoundError




    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip().startswith("#") or line.strip() == "":
                ...
            else:
                lines += 1

    print(lines)

except IndexError:
    sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit("Not a Python file")

except Exception:
    sys.exit("Too many command-line arguments")

except:
    sys.exit("File does not exist")


