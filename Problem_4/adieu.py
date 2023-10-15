import sys

names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        if len(names) == 1:
            for name in names:
                print(f"Adieu, aduei, to {name}")
        elif len(names) == 2:
            print(f"Adieu, aduei, to {names[0]} and {names[1]}")
        elif len(names) >= 3:
            print("Adieu, aduei, to ", end='')
            for name in names[0:-1]:
                print(name, ", ", end='', sep='')
            print("and", names[-1])

        sys.exit()
