def main():

    cost = 50
    payment = 0

    print(f'Amount Due: {cost}')

    while True:
        payment = int(input('Insert Coin: '))
        if coin_check(payment) == True and payment > cost:
            print("Change Owed:", abs(cost - payment))
            break
        elif coin_check(payment) == True:
            cost = cost - payment
            print(f'Amount Due: {cost}')
        else:
            print(f'Amount Due: {cost}')


def coin_check(coin):
    match coin:
        case 25 | 10 | 5:
            return True
        case _:
            return False


main()
