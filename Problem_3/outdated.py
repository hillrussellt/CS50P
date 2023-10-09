def main():
    get_and_validate_user_date()
    # convert_date(month, day, year)


def get_and_validate_user_date():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        user_date = input("Date: ")

        if user_date[0].isdigit():
            month, day, year = user_date.split("-")
            print(f"{year}-{month}-{day}")

        elif user_date[0].isalpha:
            month, day, year = user_date.split(" ")

            if month in months:
                month = months.index(month) + 1
            else:
                print("Please enter an appropriate month")
                break

            day = int(day.strip(","))
            print(f"{year}-{month:02}-{day:02}")

        else:
            break


# def convert_date(m, d, y):
#     print(f"{y}-{d}-{m}")


main()
