from typing import Tuple
from functools import lru_cache


def calculate_paths(shape: Tuple[int, int]) -> int:
    """
    Дано поле с размером rows*cols посчитать количество ходов коня из верхнего левого угла в нижний правый

    :param shape: размер доски в виде кортежа
    :return: количество путей согласно заданным условиям
    """
    ... # TODO реализуйте подсчет ходов коня
    n=shape[0]-1
    m = shape[1]-1
    d = []
    for j in range(n+1):
        a2 = []
        for i in range(m+1):
            a2.append(-1)
        d.append(a2)
    return requrc(n,m,n,m,d)

def requrc(x,y,n,m,d):
    if (x<0 or y<0 or x>n or y>m):
        return 0
    if (x==0 and y==0):
        return 1
    if d[x][y]!=-1:
        return d[x][y]

    d[x][y]=requrc(x-2,y-1,n,m,d)\
            +requrc(x-2,y+1,n,m,d)\
            +requrc(x-1,y-2,n,m,d)\
            +requrc(x+1,y-2,n,m,d) \


    return d[x][y]
if __name__ == '__main__':

    print(calculate_paths((4, 4)))  # 2
    print(calculate_paths((7, 15)))  # 13309
