"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # TODO реализовать итеративный линейный поиск
    if len(arr)==0:
        raise ValueError
    min_val=arr[0]
    i_min=0
    i=0
    for el in arr:
       if el<min_val:
           min_val=el
           i_min=i
       i+=1
    return i_min