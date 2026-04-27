from plates import is_valid


def test_tooShort():
    assert is_valid("") is False


def test_tooLong():
    assert is_valid("A") is False
