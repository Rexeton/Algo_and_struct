import random
from typing import List


def sort(container: List[int]) -> List[int]:
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
    left_conteiner=sort(container[:midle])
    right_conteiner=sort(container[midle:])
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


    # if len(container)<=1:
    #     return container
    # midle=len(container)//2
    # left_conteiner=sort(container[:midle])
    # right_conteiner=sort(container[midle:])
    # merge_container=[None]*len(container)
    # l_ind,r_ind,merge_ind=0,0,0
    # while l_ind<len(left_conteiner) and r_ind<len(right_conteiner):
    #     if left_conteiner[l_ind]<=right_conteiner[r_ind]:
    #         merge_container[merge_ind]=left_conteiner[l_ind]
    #         l_ind+=1
    #     else:
    #         merge_container[merge_ind]=right_conteiner[r_ind]
    #         r_ind+=1
    #     merge_ind += 1
    # while l_ind < len(left_conteiner):
    #     merge_container[merge_ind] = left_conteiner[l_ind]
    #     l_ind += 1
    #     merge_ind += 1
    # while r_ind<len(right_conteiner):
    #     merge_container[merge_ind]=right_conteiner[r_ind]
    #     r_ind += 1
    #     merge_ind += 1
    # return merge_container

# a=[random.randint(-100, 100) for _ in range(30)]
# b=sort(a)
# c=True
# i=0
# a=sorted(a)
# for el in a:
#    if el!=b[i]:
#        c=False
#    i+=1
# print(c)
# print(b)
# print(sorted(a))
