"""
Модуль bank_account.py
Містить реалізацію класу BankAccount для моделювання банківського рахунку.
"""

class BankAccount:
    """Клас для керування банківським рахунком."""

    def __init__(self, initial_balance: float = 0.0) -> None:
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Початковий баланс повинен бути числом.")
        if initial_balance < 0:
            raise ValueError("Початковий баланс не може бути від'ємним.")
        self._balance = float(initial_balance)

    def deposit(self, amount: float) -> float:
        """Поповнює рахунок на вказану суму."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сума поповнення повинна бути числом.")
        if amount <= 0:
            raise ValueError("Сума поповнення повинна бути більшою за нуль.")
        self._balance += float(amount)
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Знімає кошти з рахунку."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сума зняття повинна бути числом.")
        if amount <= 0:
            raise ValueError("Сума зняття повинна бути більшою за нуль.")
        if amount > self._balance:
            raise ValueError("Недостатньо коштів на балансі для зняття.")
        self._balance -= float(amount)
        return self._balance

    def get_balance(self) -> float:
        """Повертає поточний баланс."""
        return self._balance
