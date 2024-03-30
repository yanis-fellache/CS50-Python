from validator_collection import checkers



def main():
    print(validation(input("What's your email address? ")))

def validation(v):
    good = checkers.is_email(v)
    if good:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
