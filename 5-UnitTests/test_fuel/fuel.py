def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    numerator, denominator = fraction.split("/")
    x = int(numerator)
    y = int(denominator)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
