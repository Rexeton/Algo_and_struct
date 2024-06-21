from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO реализовать прямой метод расчета
    res=0
    if len(stairway)==1:
        return stairway[0]
    if len(stairway)==2:
        return stairway[2]

    for i in range(len(stairway)//2):
        res+=min(stairway[i+1],stairway[i+2])

    return res

if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3))) # 7
