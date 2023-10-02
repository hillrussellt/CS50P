def main():
    convert_this_string = input("camelCase: ")
    check_case(convert_this_string)


def check_case(input_string):
    print("snake_case: ", end='', sep='')
    for character in input_string:
        if character.isupper():
            convert_to_snake_case(character)
        else:
            print(character,  end='', sep='')


def convert_to_snake_case(letter):
    print("_", end='', sep='')
    print(letter.lower(), end='', sep='')


main()
