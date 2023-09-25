def main():
    input_time = input("What time is it? ")
    if 7 <= convert(input_time) <= 9:
        print("breakfast time")
    elif 12 <= convert(input_time) <= 13:
        print("lunch time")
    elif 18 <= convert(input_time) <= 20:
        print("dinner time")
    else:
        return


def convert(time):
    hours, minutes = time.split(":")
    converted_hours = float(hours)
    converted_minutes = float(minutes) / 60
    converted_total = float(converted_hours + converted_minutes)
    return converted_total


if __name__ == "__main__":
    main()
