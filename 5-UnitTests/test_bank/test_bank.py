from bank import value


def test_hello_lowercase():
    assert value("hello") == 0


def test_hello_capital():
    assert value("Hello") == 0
