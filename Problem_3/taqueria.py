menu_items = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def item_to_order():
    total_price = 0
    while True:

        item = input("Item to order: ").lower()

        if item in menu_items:
            continue

        try:
            total_price += menu_items[item.title()]

            if item in menu_items:
                continue

        except EOFError:
            print()
            break

        except KeyError:
            print("That item is not on the menu, please enter a valid item to order")

        print(f"Total: ${total_price:.2f}")


def main():
    item_to_order()


main()
