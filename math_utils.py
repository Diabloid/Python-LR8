def add(a: float, b: float) -> float:
    """Додає два числа."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Обидва аргументи повинні бути числами (int або float).")
    return a + b


def is_even(n: int) -> bool:
    """Перевіряє, чи є ціле число парним."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Аргумент повинен бути цілим числом (int).")
    return n % 2 == 0


def factorial(n: int) -> int:
    """Обчислює факторіал невід'ємного цілого числа."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Факторіал визначений лише для цілих чисел.")
    if n < 0:
        raise ValueError("Факторіал не визначений для від'ємних чисел.")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
