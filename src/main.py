import re
import os


def clear_names(file_names: str) -> list:
    """Функция для отчистки имен от лишних символов"""
    new_names_list = []

    # Абсолютный путь к файлу для любого ПК
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_path, "data", file_names)
    with open(full_path) as file:
        names_list = file.read().split()
        for name in names_list:
            new_name = ""
            for symbols in name:
                if symbols.isalpha():
                    new_name += symbols

            if new_name.isalpha():  # уходим от остатков пробелов
                new_names_list.append(new_name)

    return new_names_list

def is_cirillic(name_item: str) -> bool:
    """Проверка на вхождение кириллицы в строку"""
    return bool(re.search('[а-яА-Я]', name_item))


def is_english(name_item: str) -> bool:
    """Проверка на вхождение английских букв в строку"""
    return bool(re.search('[a-zA-Z]', name_item))


def filter_russian_names(names_list: list) -> list:
    """Функция выводит только русские имена из списка"""
    russian_names_list = []

    for name in names_list:
        if is_cirillic(name):
            russian_names_list.append(name)

    return russian_names_list


def filter_english_names(names_list: list) -> list:
    """Функция выводит только английские имена из списка"""
    english_names_list = []

    for name in names_list:
        if is_english(name):
            english_names_list.append(name)

    return english_names_list


def save_file(file_name:str, data: str) -> None:
    """Функция создает отдельные файлы с именами"""
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_path, "data", file_name)

    with open(full_path, "w") as name_list:
        name_list.write(data)