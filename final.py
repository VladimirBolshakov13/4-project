# 108180274
def min_platforms(weights: list, limit: int) -> int:
    """
    Функция вычисляет минимальное количество платформ, необходимых для перевозки роботов.

    :param weights: Список весов роботов.
    :param limit: Максимальный предел веса, который можно перевезти на одной платформе.
    :return: Минимальное количество платформ.
    """
    weights.sort()  # Сортируем веса роботов
    platforms = 0  # Инициализируем количество платформ
    left, right = (
        0,
        len(weights) - 1,
    )  # Указатели на самый легкий и самый тяжелый роботы

    while left <= right:
        total_weight = weights[left] + weights[right]
        # Если вес самого тяжелого и самого легкого роботов можно поместить на одну платформу, перевозим их
        if total_weight <= limit:
            left += 1
        right -= 1
        platforms += 1  # Увеличиваем количество использованных платформ

    return platforms


def main():
    """
    Основная функция программы для чтения входных данных, вызова функции min_platforms
    и вывода результата.
    """
    # Чтение входных данных
    weights = list(map(int, input().split()))
    limit = int(input())

    # Вызов функции и вывод результата
    print(min_platforms(weights, limit))


if __name__ == "__main__":
    main()
