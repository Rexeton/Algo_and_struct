# Дано: список из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом
from typing import List,Sequence
import time
from random import randint


def fast_sort(container: List[int]) -> List[int]:
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
    return fast_sort(left_conteiner)+eqval_container+fast_sort(right_conteiner)

def merge_sort(container: List[int]) -> List[int]:
    """
    Алгоритм сортировки слиянием.

    1. Если массив состоит из 1 элемента – он отсортирован
    2. Иначе массив разбивается на две части, которые сортируются рекурсивно
    3. После сортировки двух частей массива к ним применяется процедура слияния

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализуйте сортировку слиянием
    if len(container)<=1:
        return container
    midle=len(container)//2
    left_conteiner=merge_sort(container[:midle])
    right_conteiner=merge_sort(container[midle:])
    l_ind,r_ind,merge_ind=0,0,0
    while l_ind<len(left_conteiner) and r_ind<len(right_conteiner):
        if left_conteiner[l_ind]<=right_conteiner[r_ind]:
            container[merge_ind]=left_conteiner[l_ind]
            l_ind+=1
        else:
            container[merge_ind]=right_conteiner[r_ind]
            r_ind+=1
        merge_ind += 1
    while l_ind < len(left_conteiner):
        container[merge_ind] = left_conteiner[l_ind]
        l_ind += 1
        merge_ind += 1
    while r_ind<len(right_conteiner):
        container[merge_ind]=right_conteiner[r_ind]
        r_ind += 1
        merge_ind += 1
    return container

def count_sort(container: Sequence[int]) -> Sequence[int]:
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

def bubble_sort(container: Sequence[int]) -> Sequence[int]:
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



random_spis=[randint(12,25) for _ in range(10**6)]

start_time = time.perf_counter_ns()
count_sort(random_spis)
print(time.perf_counter_ns() - start_time)

random_spis=[randint(12,25) for _ in range(10**6)]
start_time = time.perf_counter_ns()
bubble_sort(random_spis)
print(time.perf_counter_ns() - start_time)

random_spis=[randint(12,25) for _ in range(10**6)]
start_time = time.perf_counter_ns()
merge_sort(random_spis)
print(time.perf_counter_ns() - start_time)

random_spis=[randint(12,25) for _ in range(10**6)]
start_time = time.perf_counter_ns()
fast_sort(random_spis)
print(time.perf_counter_ns() - start_time)