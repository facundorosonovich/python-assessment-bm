import pytest


def divide(a, b):
    try:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = a / b
        return result
    except ZeroDivisionError:
        raise ValueError("Division by zero is not allowed")


# Test cases for the divide function


def test_divide_valid():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(5, 0)
    assert str(excinfo.value) == "Division by zero is not allowed"


def test_divide_float():
    assert divide(3.0, 1.5) == 2.0
