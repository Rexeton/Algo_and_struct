from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    ...  # TODO реализовать итеративный алгоритм бинарного поиска
    if len(seq)==0:
        raise ValueError
    if value<seq[0] or value>seq[-1] or (len(seq)==1 and value!=seq[0]):
        raise ValueError
    le=len(seq)
    left=0
    right=le-1
    ind=0
    while right>left:
        center = (right+left) // 2
        if value==seq[center]:
            ind=center
            right = center - 1
            continue
        if value>seq[center]:
            left=center+1
        else:
            right=center-1
    if value==seq[left]:
        return left
    if value==seq[ind]:
        return ind
    else:
        raise ValueError

# print(binary_search(2,[]))