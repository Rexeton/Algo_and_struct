from typing import List


def stairway_path(count_stairs: int) -> List[int]:
    """
    Вычислить количество маршрутов до каждой ступени,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param count_stairs: Количество ступеней
    :return: Количество маршрутов до каждой ступени
    """
    ...  # TODO найти количество маршрутов до каждой ступени
    if not isinstance(count_stairs,int):
        raise TypeError
    if count_stairs<0:
        raise ValueError
    res=[0,1]
    if count_stairs==0:
        return [0]
    if count_stairs==1:
        return [0,1]
    stair_start,stair_finish=0,1
    for _ in range(count_stairs-1):
        stair_start, stair_finish=stair_finish,stair_start+stair_finish
        res.append(stair_finish)
    return res

if __name__ == '__main__':
    print(stairway_path(0))  # [0]
    print(stairway_path(5))  # [0, 1, 1, 2, 3, 5]
