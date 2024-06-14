from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Алгоритм быстрой сортировки.

    1. Выбираем опорный элемент. Например, первый элемент.
    2. В левую часть отправляем всё что меньше опорного элемента, в правую всё что больше.
    3. К левой и правой части рекурсивно применяет алгоритм быстрой сортировки.

    :param container: последовательность, которую надо отсортировать
    :return: Отсортированная в порядке возрастания последовательность
    """
    ...  # TODO реализовать алгоритм быстрой сортировки
    if len(container)<=1:
        return container
    midle=container[len(container)//2]
    left_conteiner=[]
    right_conteiner=[]
    eqval_container=[]
    for el in container:
        if el>midle:
            right_conteiner.append(el)
        elif el<midle:
            left_conteiner.append(el)
        else:
            eqval_container.append(el)
    return sort(left_conteiner)+eqval_container+sort(right_conteiner)

