"""
Модуль test_math_utils.py
Unit-тести для модуля math_utils з використанням фреймворку pytest.
(Альтернативна реалізація до test_math_utils_unittest.py для порівняння).
"""

import pytest
from math_utils import add, is_even, factorial


# --- Тести для функції add ---
def test_add_positive():
    assert add(5, 7) == 12
    assert add(20, 30) == 50


def test_add_negative_and_zero():
    assert add(-4, -6) == -10
    assert add(-5, 5) == 0
    assert add(0, 0) == 0


def test_add_float_values():
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert add(2.5, 3.5) == 6.0


def test_add_invalid_input_types():
    with pytest.raises(TypeError):
        add("10", 5)
    with pytest.raises(TypeError):
        add([1], 2)


# --- Тести для функції is_even ---
def test_is_even_true():
    assert is_even(4) is True
    assert is_even(0) is True
    assert is_even(1002) is True


def test_is_even_false():
    assert is_even(3) is False
    assert is_even(99) is False
    assert is_even(-15) is False


def test_is_even_negative_even():
    assert is_even(-2) is True
    assert is_even(-100) is True


def test_is_even_type_error():
    with pytest.raises(TypeError):
        is_even(2.0)
    with pytest.raises(TypeError):
        is_even("2")
    with pytest.raises(TypeError):
        is_even(True)


# --- Тести для функції factorial ---
def test_factorial_base_cases():
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_factorial_positive_values():
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(7) == 5040


def test_factorial_negative_value_error():
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(-5)


def test_factorial_invalid_types():
    with pytest.raises(TypeError):
        factorial(4.5)
    with pytest.raises(TypeError):
        factorial("4")
    with pytest.raises(TypeError):
        factorial(False)
