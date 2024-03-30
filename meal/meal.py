
def main():
    tm = input("What time is it? ")
    time = convert(tm)
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    time = float(minutes)/60 + float(hours)
    return float(time)

if __name__ == "__main__":
    main()
