def main():
    time = input("time: ")
    if ":" in time:
        c_time = textToHour(time)
        if c_time >= 7 and c_time <= 8:
            print("Breakfast time")
        elif c_time >= 12 and c_time <= 13:
            print("Lunch time")
        elif c_time >= 18 and c_time <= 19:
            print("Dinner time")


def textToHour(time):
    hours, mins = time.split(":")
    hours_int = int(hours)
    return hours_int


if __name__ == "__main__":
    main()
