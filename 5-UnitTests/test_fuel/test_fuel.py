import pytest

from fuel import convert, gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_convert_nonInteger():
    with pytest.raises(ValueError):
        convert("a/2")
