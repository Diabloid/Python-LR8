import json
from typing import List, Dict, Any


def read_users(filepath: str) -> List[Dict[str, Any]]:
    """Зчитує список користувачів із JSON-файлу."""
    if not isinstance(filepath, str):
        raise TypeError("Шлях до файлу повинен бути рядком.")
    
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("Вміст JSON-файлу повинен бути списком об'єктів.")

    return data


def filter_users_by_age(users: List[Dict[str, Any]], min_age: int) -> List[Dict[str, Any]]:
    """Повертає список користувачів, вік яких перевищує min_age."""
    if not isinstance(users, list):
        raise TypeError("Список користувачів повинен бути типу list.")
    if isinstance(min_age, bool) or not isinstance(min_age, int):
        raise TypeError("Мінімальний вік повинен бути цілим числом.")
    if min_age < 0:
        raise ValueError("Мінімальний вік не може бути від'ємним.")

    filtered = []
    for user in users:
        if isinstance(user, dict) and "age" in user and isinstance(user["age"], (int, float)):
            if user["age"] > min_age:
                filtered.append(user)
    return filtered


def save_users(filepath: str, data: List[Dict[str, Any]]) -> bool:
    """Зберігає список користувачів у JSON-файл."""
    if not isinstance(filepath, str):
        raise TypeError("Шлях до файлу повинен бути рядком.")
    if not isinstance(data, list):
        raise TypeError("Дані для збереження повинні бути списком.")

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return True
