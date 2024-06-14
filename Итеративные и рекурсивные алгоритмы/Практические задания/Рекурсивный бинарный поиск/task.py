from typing import Sequence


def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать алгоритм бинарного поиска
    if right_border is None or right_border>len(seq)-1:
        right_border=len(seq)-1
    if len(seq)==0:
        raise ValueError
    if seq[left_border]==value:
        return left_border
    if right_border<=left_border:
        raise ValueError
    center = (right_border + left_border) // 2
    if value==seq[left_border]:
        return left_border
    else:
        if value<=seq[center] :
            return binary_search(value,seq,left_border,center)
        else:
            return binary_search(value, seq,  center+1 ,right_border)

# print(binary_search(1,[]))
# print(binary_search(100,[i for i in range(100)] + [101]))
