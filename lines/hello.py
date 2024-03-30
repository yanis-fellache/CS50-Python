def main():
    #Get the name
    name = input("What's your name")
    #Run Hello
    print(hello(name))


def hello(person):
    #return sentence
    return f"Hello {person}, how are you"

#call main
if __name__ == "__main__":
    main()