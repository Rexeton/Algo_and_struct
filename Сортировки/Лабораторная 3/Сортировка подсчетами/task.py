from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами


    help_dikt={}
    max_el=0
    for i in range(len(container)):
        max_el=max(max_el,container[i])
        if container[i] in help_dikt:
            help_dikt[container[i]]+=1
        else:
            help_dikt[container[i]]=1
    res=[]
    for i in range(0, max_el + 1):
        if i in help_dikt:
            for _ in range(help_dikt[i]):
                res.append(i)

    return res

    # return [[i]*help_dikt[container[i]] for i in [i in range(0,max_el+1)] \
    #         if i in help_dikt]

print(sort([5,0,8,9,55,9]))