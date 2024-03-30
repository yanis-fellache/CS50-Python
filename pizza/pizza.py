from tabulate import tabulate
import sys
import csv

try:
    if len(sys.argv) < 2:
        raise IndexError
    elif len(sys.argv) > 2:
        raise Exception
    elif not sys.argv[1].endswith(".csv"):
        raise FileNotFoundError

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))



except IndexError:
    sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit("Not a Python file")

except Exception:
    sys.exit("Too many command-line arguments")

except:
    sys.exit("File does not exist")

