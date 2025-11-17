import re
import os

# base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_path)
# full_path = os.path.join(base_path, 'data', 'names.txt')
# print(full_path)

def clear_names(file_names: str) -> list:
    """Функция для отчистки имен от лишних символов"""
    new_names_list = []

    # Абсолютный путь к файлу для любого ПК
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_path, 'data', file_names)
    with open(full_path) as file:
        names_list = file.read().split()
        for name in names_list:
            new_name = ''
            for symbols in name:
                if symbols.isalpha():
                    new_name += symbols

            if new_name.isalpha(): # уходим от остатков пробелов
                new_names_list.append(new_name)

    return new_names_list

cleared_names = clear_names('names.txt')
for name in cleared_names:
    print(name)