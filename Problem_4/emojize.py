import emoji


def get_text():
    text = input("Input: ")
    return text


def emoji_convert(emoji_text):

    print(emoji.emojize(emoji_text, language="alias"))


def main():
    text = get_text()
    emoji_convert(text)


main()
