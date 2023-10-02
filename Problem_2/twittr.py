def main():
    message = input("Input: ")
    remove_vowels_from(message)


def remove_vowels_from(input_string):
    for character in input_string:
        match character.lower():
            case "a" | "e" | "i" | "o" | "u":
                continue
            case _:
                print(character, end='')


main()
