def main():
    name = input("What's your name")
    string = goodbye(name)
    print(string)

def goodbye(person):
    return f"Goodbye {person}, I hope you had a great day"

if __name__ == "__main__":
    main()