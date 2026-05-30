from py_starter.math_utils import add, multiply


def test_add() -> None:
    assert add(2, 3) == 5


def test_multiply() -> None:
    assert multiply(6, 7) == 42
