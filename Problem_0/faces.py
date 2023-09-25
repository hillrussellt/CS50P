def main():
    convert()


def convert():
    prompt = str("Please type a string with a smiley! ")
    response = input(prompt)
    print(response.replace(":)", "🙂").replace(":(", "🙁"))


main()
