# TODO решите задачу

import json

def calculate_score_sum(json_file_path):
    # Читаем содержимое JSON файла
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Инициализируем сумму
    total_sum = 0.0

    # Обрабатываем каждый словарь в списке
    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)
        total_sum += score * weight

    # Возвращаем результат, округленный до 3 знаков после запятой
    return round(total_sum, 3)

# Вызов функции
if __name__ == "__main__":
    json_file_path = 'input.json'  # Укажите путь к вашему JSON файлу
    result = calculate_score_sum(json_file_path)
    print(result)