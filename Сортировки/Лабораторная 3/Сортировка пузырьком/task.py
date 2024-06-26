from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки пузырьком

    flag_of_iter=True
    ite=0
    while flag_of_iter:
        flag_of_iter=False
        for i in range(1,len(container)-ite):
            if container[i]<container[i-1]:
                flag_of_iter=True
                container[i] , container[i - 1]=container[i-1] , container[i]
        ite+=1
    return container
