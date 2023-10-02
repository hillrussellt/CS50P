def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):

    # print(string[2:(len(string)-1)])

    if len(string) > 6 or len(string) < 2 or not string.isalnum():
        return False
    elif not string[0:2].isalpha():
        return False
    elif string[2:(len(string)-1)].isdigit() and string[-1].isalpha() or not string[2:(len(string))].isdigit():
        return False
    elif string[2] == "0":
        return False
    return True


main()
