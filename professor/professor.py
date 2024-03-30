import random


def main():
    score = 0
    level = get_level()
    turn = 10
    while turn > 0:
        x, y = generate_integer(level)
        z = x + y
        false = 3
        while false > 0:
            userAnswer = input(str(x) + " + " + str(y) + " = ")
            try:
                if int(userAnswer) == z:
                    score +=1
                    break
                else:
                    raise ValueError

            except ValueError:
                print("EEE")
                false -= 1
        if false == 0:
            print(z)
        turn -= 1

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level

            else:
                raise ValueError
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randrange(0,10)
        y = random.randrange(0,10)
    elif level == 2:
        x = random.randrange(10,100)
        y = random.randrange(10,100)
    elif level == 3:
        x = random.randrange(100,1000)
        y = random.randrange(100,1000)

    return x, y





if __name__ == "__main__":
    main()
