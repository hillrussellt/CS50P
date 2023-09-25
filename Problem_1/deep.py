def main():
    question()


def question():
    answer = str(input(
        "What is the answer to the Great Question of Life, the Universe, and Everything? ")).strip().lower()
    match answer:
        case "42" | "fourty-two" | "fourty two":
            print("Yes")
        case _:
            print("No")


main()
