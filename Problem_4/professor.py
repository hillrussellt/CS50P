import random


def main():
    get_level()
    generate_integer(4)


def get_level():

    valid_levels = [1, 2, 3]
    while True:
        level = int(input("Level: "))
        try:
            if level in valid_levels:
                break
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(number_of_problems):
    random.seed()
    correct = 0

    for _ in range(number_of_problems):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        answer = int(input(f"{x} + {y} = "))

        if x + y == answer:
            correct += 1
        else:
            wrong_count = 0
            while wrong_count < 2:
                wrong_count += 1
                print("EEE")
                input(f"{x} + {y} = ")
            else:
                print(f"{x} + {y} = {x+y}")

    print(f"Score: {correct}")


if __name__ == "__main__":
    main()
