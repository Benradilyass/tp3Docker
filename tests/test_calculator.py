import pytest
from app.calculator import add, multiply


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-4, -6) == -10


def test_add_with_zero():
    assert add(5, 0) == 5


def test_multiply_positive_numbers():
    assert multiply(4, 3) == 12


def test_multiply_negative_numbers():
    assert multiply(-2, 5) == -10


def test_multiply_with_zero():
    assert multiply(7, 0) == 0