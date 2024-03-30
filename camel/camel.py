camelCase = input("camelCase: ")
list = list(camelCase)
for letter in list:
    if letter.islower() == False:
        letter = letter.lower()
        letter = "_" + letter
    print(letter, end = "")


