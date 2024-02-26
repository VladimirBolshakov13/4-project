# 108021260
from typing import List


def min_platforms(weights: List[int], limit: int) -> int:
    weights.sort()  # Сортируем веса роботов
    platforms = 0  # Инициализируем количество платформ
    # Указатели на самый легкий и самый тяжелый роботы
    left, right = 0, len(weights) - 1

    while left <= right:
        # сли самый тяжелый и самый легкий роботы можно поместить на одну платформу, перевозим их
        if weights[left] + weights[right] <= limit:
            left += 1
            right -= 1
        else:
            # Если не получается, перевозим только самого тяжелого робота
            right -= 1
        platforms += 1  # Увеличиваем количество использованных платформ

    return platforms


# Чтение входных данных
weights = list(map(int, input().split()))
limit = int(input())

# Вызов функции и вывод результата
print(min_platforms(weights, limit))
