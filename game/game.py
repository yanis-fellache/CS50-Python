import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break

    except:
        pass

number = random.randrange(1,n + 1)

while True:
    try:
        guess = int(input("Guess: "))

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        elif guess == number:
            print("Just right!")
            break
        else:
            raise Exception

    except:
        pass

