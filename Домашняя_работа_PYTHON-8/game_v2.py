"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def binary_predict(number: int = 1) -> int:
    """Бинарный алгоритм угадывания числа
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    lower_bound = 1
    upper_bound = 100

    while True:
        count += 1
        # Предполагаемое число — среднее между границами
        predict_number = (lower_bound + upper_bound) // 2  
        
        if number == predict_number:  # Угадали
            break
        elif number < predict_number:  # Загаданное число меньше
            upper_bound = predict_number - 1  # Обновляем верхнюю границу
        else:  # Загаданное число больше
            lower_bound = predict_number + 1  # Обновляем нижнюю границу

    return count

def score_game(predict_function) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        predict_function ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(49)
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел
    for number in random_array:
        count_ls.append(predict_function(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(binary_predict)
