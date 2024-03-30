def main():
    while True:
        try:
            fraction = input("What's the fraction? ")
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = fraction.split("/")
    total = int(x) / int(y)
    return total


def gauge(percentage):
    if percentage <= 0.01:
        return "E"
    elif percentage >= 0.99:
        return "F"
    else:
        rounded = round(percentage * 100)
        return str(rounded) + "%"


if __name__ == "__main__":
    main()



