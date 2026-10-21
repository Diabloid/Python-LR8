"""
Модуль test_bank_account.py
Unit-тести для класу BankAccount з використанням unittest, setUp() та tearDown().
"""

import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Ініціалізація тестового банківського рахунку перед кожним тестом."""
        self.initial_amount = 100.0
        self.account = BankAccount(self.initial_amount)

    def tearDown(self):
        """Очищення ресурсів після виконання тесту."""
        self.account = None

    # --- Перевірка початкового балансу ---
    def test_default_initial_balance(self):
        default_account = BankAccount()
        self.assertEqual(default_account.get_balance(), 0.0)

    def test_custom_initial_balance(self):
        self.assertEqual(self.account.get_balance(), self.initial_amount)

    def test_negative_initial_balance_raises_error(self):
        with self.assertRaises(ValueError):
            BankAccount(-50.0)

    def test_invalid_type_initial_balance(self):
        with self.assertRaises(TypeError):
            BankAccount("one hundred")

    # --- Позитивні сценарії (deposit, withdraw) ---
    def test_deposit_valid_amount(self):
        new_balance = self.account.deposit(50.0)
        self.assertEqual(new_balance, 150.0)
        self.assertEqual(self.account.get_balance(), 150.0)

    def test_deposit_multiple_times(self):
        self.account.deposit(25.0)
        self.account.deposit(75.0)
        self.assertEqual(self.account.get_balance(), 200.0)

    def test_withdraw_valid_amount(self):
        new_balance = self.account.withdraw(40.0)
        self.assertEqual(new_balance, 60.0)
        self.assertEqual(self.account.get_balance(), 60.0)

    def test_withdraw_exact_full_balance(self):
        new_balance = self.account.withdraw(100.0)
        self.assertEqual(new_balance, 0.0)
        self.assertEqual(self.account.get_balance(), 0.0)

    # --- Негативні сценарії (ValueError, TypeError) ---
    def test_deposit_negative_or_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)
        with self.assertRaises(ValueError):
            self.account.deposit(-30.0)

    def test_deposit_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.deposit("50")

    def test_withdraw_more_than_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150.0)
        # Переконуємось, що баланс не змінився після невдалої спроби
        self.assertEqual(self.account.get_balance(), 100.0)

    def test_withdraw_negative_or_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)
        with self.assertRaises(ValueError):
            self.account.withdraw(-10.0)

    def test_withdraw_invalid_type(self):
        with self.assertRaises(TypeError):
            self.account.withdraw(None)


if __name__ == "__main__":
    unittest.main()
