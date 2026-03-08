import random


def main():
    correct_answers_count = 0
    wrong_answers_count = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        try:
            user_answer = int(input(f"{x} + {y} ="))
            if user_answer == x + y:
                correct_answers_count += 1
                wrong_answers_count = 0
            else:
                print("EEE")
                wrong_answers_count += 1
                while 0 < wrong_answers_count < 3:
                    user_answer = int(input(f"{x} + {y} ="))
                    if user_answer == x + y:
                        correct_answers_count += 1
                        wrong_answers_count = 0
                    else:
                        print("EEE")
                        wrong_answers_count += 1
                print(f"{x} + {y} = {x + y}")
        except ValueError:
            print("EEE")
    print("Score:", correct_answers_count)


def get_level():
    while True:
        try:
            user_level = int(input("Level: "))
            if user_level == 1 or user_level == 2 or user_level == 3:
                return user_level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    elif level == 3:
        number = random.randint(100, 999)
    else:
        raise ValueError
    return number


if __name__ == "__main__":
    main()
