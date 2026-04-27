def main():
    text_novowels = input("Input text: ")
    print(shorten(text_novowels))


def shorten(word):

    return (
        word.replace("a", "")
        .replace("e", "")
        .replace("i", "")
        .replace("o", "")
        .replace("u", "")
        .replace("A", "")
        .replace("E", "")
        .replace("I", "")
        .replace("O", "")
        .replace("U", "")
    )


if __name__ == "__main__":
    main()
