def main():
    evaluate()


def evaluate():
    x, operation, z = input("Expression: ").strip().split(' ')

    x = float(x)
    z = float(z)

    if operation == "+":
        print(float(x + z))
    elif operation == "-":
        print(float(x - z))
    elif operation == "*":
        print(float(x * z))
    else:
        print(float(x / z))


main()
