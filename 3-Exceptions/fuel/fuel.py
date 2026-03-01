def main():
    fraction = get_int()
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")


def get_int():
    while True:
        try:
            fraction = input("input fraction: ")
            numerator, denominator = fraction.split("/")
            top = int(numerator)
            bottom = int(denominator)
            division = top / bottom
            result = int(division * 100)
            if result > 100:
                raise ValueError()
        except (ValueError, ZeroDivisionError):
            print("Please enter valid fraction: ")
        else:
            break
    return result


main()
