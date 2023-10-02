def main():
    user_fruit = input("Item: ")
    available_fruits = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew melon": "50",
        "kiwifruit": "90",
        "lemon": "15",
        "lime": "20",
        "nectarine": "60",
        "orange": "80",
        "peach": "60",
        "pear": "100",
        "pineapple": "50",
        "plums": "70",
        "strawberries": "50",
        "sweet cherries": "100",
        "tangarine": "50",
        "watermelon": "80",
    }

    if user_fruit.lower() in available_fruits.keys():
        print("Calories: " + available_fruits[user_fruit.lower()])


main()
