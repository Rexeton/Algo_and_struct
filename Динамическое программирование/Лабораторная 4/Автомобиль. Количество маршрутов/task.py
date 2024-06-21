from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования
    n-=1
    m -= 1
    d = []
    for j in range(n+1):
        a2 = []
        for i in range(m+1):
            a2.append(-1)
        d.append(a2)
    return requrc(n,m,n,m,d)

def requrc(x,y,n,m,d):
    print(x,y,n,m,d)
    if (x<0 or y<0 or x>n or y>m):
        return 0
    if (x==0 and y==0):
        return 1
    if d[x][y]!=-1:
        return d[x][y]

    d[x][y]=requrc(x-1,y-1,n,m,d)\
            +requrc(x-1,y,n,m,d)\
            +requrc(x,y-1,n,m,d)\

if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
