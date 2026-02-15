def main():
    greeting = input("")
    convert(greeting)


def convert(greeting):
    greeting = greeting.replace(":)", "🙂")
    greeting = greeting.replace(":(", "🙁")

    print(greeting)


main()
