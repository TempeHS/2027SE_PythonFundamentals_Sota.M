cost = 50
amount_left_to_pay = cost


while amount_left_to_pay > 0:
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amount_left_to_pay -= coin
        if amount_left_to_pay > 0:
            print("Amount Due:", amount_left_to_pay)
        elif amount_left_to_pay <= 0:
            change = abs(amount_left_to_pay)
            print("Change:", change)
    else:
        print("Amount Due: 50")
