while True:
    fuel_in_tank = input("Fraction: ")

    try:
        x, y = fuel_in_tank.split("/")
    except ValueError:
        print("Please provide two numbers.")
        continue

    try:
        x = int(x)
    except ValueError:
        print("numerator is not an int")
        continue

    try:
        y = int(y)
    except ValueError:
        print("denominator is not an int")
        continue

    try:
        int(int(x) / int(y))
    except (ZeroDivisionError, TypeError, ValueError):
        print("Can't divide by zero nerd.")
        continue

    try:
        if x > y:
            print("x cannot be greater than y")
    except TypeError:
        print("X is greater than y is not allowed.")
        continue

percent = x / y * 100

if percent <= 1:
    print("E")
if percent >= 99:
    print("F")

print(f"{round(percent)}%")
