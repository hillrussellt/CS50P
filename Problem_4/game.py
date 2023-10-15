import random
import sys

random.seed()


def main():
    while True:
        try:
            user_num = int(input("Level: "))
        except ValueError:
            continue

        if type(user_num) == int and user_num > 0:
            start_guessing(user_num)
        else:
            continue


def start_guessing(user_number_from_main):
    try:
        random_num = random.randrange(1, user_number_from_main)
    except ValueError:
        random_num = 1
    else:
        random_num = random.randrange(1, user_number_from_main)

    while True:
        try:
            user_guess = int(input("Guess: "))
        except ValueError:
            continue
        else:
            if user_guess == random_num:
                sys.exit("Just right!")
            elif user_guess < random_num:
                print("Too low")
            elif user_guess > random_num:
                print("Too high")


main()
