"""
Модуль test_math_utils_unittest.py
Unit-тести для модуля math_utils з використанням вбудованої бібліотеки unittest.
"""

import unittest
from math_utils import add, is_even, factorial


class TestMathUtilsUnittest(unittest.TestCase):
    # --- Тести для add ---
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(100, 250), 350)

    def test_add_negative_and_zero(self):
        self.assertEqual(add(-5, -7), -12)
        self.assertEqual(add(-10, 10), 0)
        self.assertEqual(add(0, 0), 0)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.3), 3.8)
        self.assertAlmostEqual(add(-0.5, 0.5), 0.0)

    def test_add_invalid_types(self):
        with self.assertRaises(TypeError):
            add("2", 3)
        with self.assertRaises(TypeError):
            add(None, 5)

    # --- Тести для is_even ---
    def test_is_even_with_even_numbers(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(100))
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_numbers(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(13))
        self.assertFalse(is_even(-7))

    def test_is_even_with_negative_even_numbers(self):
        self.assertTrue(is_even(-2))
        self.assertTrue(is_even(-44))

    def test_is_even_invalid_type(self):
        with self.assertRaises(TypeError):
            is_even(3.14)
        with self.assertRaises(TypeError):
            is_even("4")
        with self.assertRaises(TypeError):
            is_even(True)

    # --- Тести для factorial ---
    def test_factorial_zero_and_one(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive_numbers(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_factorial_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_factorial_invalid_types_raises_type_error(self):
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial(False)


if __name__ == "__main__":
    unittest.main()
