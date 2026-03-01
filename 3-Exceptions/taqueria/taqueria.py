menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
print(menu)

total = 0
while True:
    try:
        orderItem = input("What would you like to order? ").strip().title()
        if orderItem in menu:
            # print("price: ", menu[orderItem])
            price = menu[orderItem]
            total += price
            print(f"${total:.2f}")
    # on windows / cloud is ctrl + z
    except EOFError:
        print()
