list = {}

while True:
    try:
        item = input().strip().upper()
        list[item] += 1
    except KeyError:
        list[item] = 1
    except EOFError:
        sorted_list = sorted(list.items())
        for key, value in sorted_list:
            print(f"{value} {key.upper()}")
        print("\n")
        break
