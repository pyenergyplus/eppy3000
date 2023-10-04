"""sample template for tests"""
# copy this and use when you are doing tests
import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),  # a, b, expected
    ],
)
def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected
