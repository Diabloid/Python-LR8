import json
from unittest.mock import patch, mock_open
import pytest
from data_manager import read_users, filter_users_by_age, save_users


# Тестові дані користувачів
SAMPLE_USERS = [
    {"id": 1, "name": "Олексій", "age": 17},
    {"id": 2, "name": "Марія", "age": 20},
    {"id": 3, "name": "Богдан", "age": 25},
    {"id": 4, "name": "Оксана", "age": 35},
    {"id": 5, "name": "Тарас", "age": 50},
]


# Тести з використанням mock для зчитування даних
def test_read_users_success():
    fake_json = json.dumps(SAMPLE_USERS, ensure_ascii=False)
    with patch("builtins.open", mock_open(read_data=fake_json)) as mocked_file:
        result = read_users("users.json")

        mocked_file.assert_called_once_with("users.json", "r", encoding="utf-8")
        assert len(result) == 5
        assert result[0]["name"] == "Олексій"
        assert result[1]["age"] == 20


def test_read_users_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_users("non_existent.json")


def test_read_users_invalid_json():
    with patch("builtins.open", mock_open(read_data="некоректний {json")):
        with pytest.raises(json.JSONDecodeError):
            read_users("broken.json")


def test_read_users_not_a_list():
    fake_dict_json = json.dumps({"status": "ok"})
    with patch("builtins.open", mock_open(read_data=fake_dict_json)):
        with pytest.raises(ValueError):
            read_users("dict.json")


def test_read_users_invalid_filepath_type():
    with pytest.raises(TypeError):
        read_users(123)


# Тести збереження у файл з перевіркою mock викликів
def test_save_users_success():
    users_to_save = [{"id": 10, "name": "Іван", "age": 28}]
    mocked_file = mock_open()

    with patch("builtins.open", mocked_file):
        status = save_users("output.json", users_to_save)

        assert status is True
        mocked_file.assert_called_once_with("output.json", "w", encoding="utf-8")
        handle = mocked_file()
        handle.write.assert_called()


def test_save_users_invalid_filepath():
    with pytest.raises(TypeError):
        save_users(None, SAMPLE_USERS)


def test_save_users_invalid_data_type():
    with pytest.raises(TypeError):
        save_users("output.json", "not a list")


# Параметризовані тести для фільтрації користувачів за віком
@pytest.mark.parametrize(
    "min_age, expected_count, expected_names",
    [
        (0, 5, ["Олексій", "Марія", "Богдан", "Оксана", "Тарас"]),
        (17, 4, ["Марія", "Богдан", "Оксана", "Тарас"]),
        (20, 3, ["Богдан", "Оксана", "Тарас"]),
        (30, 2, ["Оксана", "Тарас"]),
        (50, 0, []),
    ],
)
def test_filter_users_by_age_parametrized(min_age, expected_count, expected_names):
    filtered = filter_users_by_age(SAMPLE_USERS, min_age)
    assert len(filtered) == expected_count
    assert [user["name"] for user in filtered] == expected_names


# Параметризовані тести некоректних значень для filter_users_by_age
@pytest.mark.parametrize("invalid_age", [-1, -10, -100])
def test_filter_users_negative_age_raises_value_error(invalid_age):
    with pytest.raises(ValueError):
        filter_users_by_age(SAMPLE_USERS, invalid_age)


@pytest.mark.parametrize("invalid_type_age", ["20", 25.5, True, False, None, [18]])
def test_filter_users_invalid_type_raises_type_error(invalid_type_age):
    with pytest.raises(TypeError):
        filter_users_by_age(SAMPLE_USERS, invalid_type_age)


def test_filter_users_invalid_users_list():
    with pytest.raises(TypeError):
        filter_users_by_age("not a list", 20)


def test_filter_users_skips_invalid_user_objects():
    corrupted_data = [
        {"id": 1, "name": "Valid", "age": 25},
        "not a dict",
        {"id": 2, "name": "No age"},
        {"id": 3, "name": "Wrong age type", "age": "thirty"},
    ]
    filtered = filter_users_by_age(corrupted_data, 20)
    assert len(filtered) == 1
    assert filtered[0]["name"] == "Valid"
