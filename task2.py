

import csv
import json

def csv_to_json(csv_file_path, delimiter=",", line_terminator="\n"):

    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:  # Открываем файл, указываем кодировку
            reader = csv.DictReader(csvfile, delimiter=delimiter)  # Используем DictReader для словарей

            # Читаем все строки CSV.
            data = list(reader)

        # Преобразуем в JSON строку с отступами
        json_string = json.dumps(data, indent=4)
        return json_string

    except FileNotFoundError:
        print(f"Ошибка: файл '{csv_file_path}' не найден.")
        return None
    except Exception as e:  #Обработка других возможных исключений
        print(f"Произошла ошибка: {e}")
        return None


# Пример использования:
csv_filepath = "input.csv"  # Замените на путь к вашему CSV файлу
json_output = csv_to_json(csv_filepath)

if json_output:
    print(json_output)
