def main():
    sentence = input("Input: ")
    print(shorten(sentence))

def shorten(word):
    word = word.lower()
    word = word.replace("a","")
    word = word.replace("e","")
    word = word.replace("i","")
    word = word.replace("o","")
    word = word.replace("u","")
    word = word.replace("y","")
    return word

if __name__ == "__main__":
    main()