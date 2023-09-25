def main():
    dollars = dollars_to_float(
        input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    stripped_and_rounded = float(str(d).strip("$"))
    return (stripped_and_rounded)


def percent_to_float(p):
    stripped_and_converted = float(str(p).strip("%"))/100
    return (stripped_and_converted)


main()
