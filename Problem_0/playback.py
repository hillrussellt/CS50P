def main():
    prompt = str("Please type a sentence for me to augment. ")
    statement = input(prompt)
    print(statement.replace(" ", "..."))


main()
