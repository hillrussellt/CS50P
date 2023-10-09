def main():
    generate_list()


def generate_list():
    grocery_list = {
    }

    while True:
        try:
            item = input().upper()
            if item in grocery_list:
                grocery_list[item] = grocery_list[item] + 1
            else:
                grocery_list[item] = 1

        except EOFError:
            sorted_list = dict(sorted(grocery_list.items()))
            for i in sorted_list:
                print(f"{sorted_list[i]} {i}\n", end='')


main()
