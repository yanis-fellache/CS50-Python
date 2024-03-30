import csv
import sys

counter = 0
try:
    open(sys.argv[2],"w").close()
    with open(sys.argv[2], "a") as f:
        writer = csv.writer(f)

        if len(sys.argv) < 3:
            raise IndexError
        elif len(sys.argv) > 3:
            raise Exception
        elif not sys.argv[1].endswith(".csv"):
            raise FileNotFoundError
        elif not sys.argv[2].endswith(".csv"):
            raise FileNotFoundError

        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "name":
                    writer.writerow(["first", "last", "house"])
                else:
                    last_name, first_name = row[0].split(",")
                    writer.writerow([first_name.lstrip(), last_name, row[1]])






except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("Not a Python file")
except Exception:
    sys.exit("Too many command-line arguments")
except:
    sys.exit(f"Could not read {sys.argv[1]}")
