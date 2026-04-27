from twttr import shorten


def main():
    test_shorten()


def test_shorten():
    assert shorten("word") == "wrd"


if __name__ == "__main__":
    main()
