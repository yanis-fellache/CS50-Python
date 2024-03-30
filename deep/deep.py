a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")


if a.strip() == "42" or a.lower().strip() == "forty two" or a.lower().strip() == "forty-two":
    print("Yes")
else:
    print("No")