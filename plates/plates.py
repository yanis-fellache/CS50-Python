def main():
    plate = input("Plate: ")
    plate = list(plate)
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    #Requirement 1: Checking that lenght of str is between 2 and 6 char
    if len(plate) < 2 or len(plate) > 6:
        return False

    #Requirement 2: Checking that first 2 char are letters
    if plate[0].isdigit() or plate[1].isdigit():
        return False


    #Requirement 3.1: Checking that there are no numbers in middle of word
    encountered = False
    for x in plate:
        if x.isdigit():
            encountered = True
        elif encountered and x.isalpha():
            return False

    #Requirement 3.2: Checking that first number is not 0
    for char in plate:
        if char.isdigit():
            if char == "0":
                return False

    #Requirement 4: Checking that there is only letters and numbers in str
    y = 0
    for z in plate:
        if z.isalpha() or z.isdigit():
            None
        else:
            y += 1
    if y > 0:
        return False

    return True



if __name__ == "__main__":
    main()

