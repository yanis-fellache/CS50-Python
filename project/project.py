import random
import sys



def main():
    print("Welcome to Hangman! Try to guess the word. If stuck, a single-use hint is available by typing 'hint'")
    hangman(choose_word(input("Choose the difficulty of the word (3-7 letters): ")))



def choose_word(d):
    try:
        name_file = f"{d}-letter-words.txt"
        with open(name_file, "r") as file:
            lines = file.readlines()
        word = random.choice(lines).strip().lower()
        return word
    except:
        if int(d) not in range(3, 8):
            sys.exit("Not a level")

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def fail(attempts):
    stages = [
        r'''
         -----
         |   |
             |
             |
             |
             |
        ------
        ''',
        r'''
         -----
         |   |
         O   |
             |
             |
             |
        ------
        ''',
        r'''
         -----
         |   |
         O   |
         |   |
             |
             |
        ------
        ''',
        r'''
         -----
         |   |
         O   |
        /|   |
             |
             |
        ------
        ''',
        r'''
         -----
         |   |
         O   |
        /|\  |
             |
             |
        ------
        ''',
        r'''
         -----
         |   |
         O   |
        /|\  |
        /    |
             |
        ------
        ''',
        r'''
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
        ------
        '''
    ]
    stage = stages[attempts - 1]
    return stage


def hint(word, gl):
    while True:
        h = random.choice(word)
        if h in gl:
            continue
        else:
            return h







def hangman(word):

    guessed_letters = []
    attempts = 0
    hint_list = []

    while attempts < 7:
        current_display = display_word(word, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Already guessed letters:", *guessed_letters)

        guess = input("Guess a letter: ").lower()
        print()

        if guess == "hint":
            hint_list.append(hint(word, guessed_letters))
            if len(hint_list) > 1:
                print("Hint was already used.")
            elif current_display.count('_') == 1:
                print("Only one letter left.")
            else:
                guess = hint_list[0]
                print("Here you go:")

        if guess == word:
            if attempts == 0:
                sys.exit("AMAZING! You won first try! Congratulations")
            else:
                sys.exit("Congratulations! You guessed the word: " + word)

        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")

        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")

        else:
            guessed_letters.append(guess)

            if guess not in word:
                print("Incorrect guess!")
                attempts += 1
                print(fail(attempts))

            if "_" not in display_word(word, guessed_letters):
                if attempts == 0:
                    sys.exit("AMAZING! You won with no mess up! Congratulations")
                else:
                    sys.exit("Congratulations! You guessed the word: " + word)


    if "_" in display_word(word, guessed_letters):
        sys.exit("Sorry, you ran out of attempts. The word was: " + word)


if __name__ == "__main__":
    main()
