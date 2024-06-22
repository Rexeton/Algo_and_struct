from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования
    d = []
    for j in range(n):
        a2 = []
        for i in range(m):
            a2.append(0)
        d.append(a2)
    requrc(n-1, m-1, n-1, m-1, d)
    return d
def requrc(x,y,n,m,d):
    if (x<0 or y<0):
        return 0
    if (x==0 and y==0):
        d[x][y]=1
        return d[x][y]

    d[x][y]=requrc(x-1,y,n,m,d)+requrc(x,y-1,n,m,d)+requrc(x-1,y-1,n,m,d)
    for i in range(n+1):
        print([d[i][j] for j in range(m+1)])
    print('\n')

    #print(f'{x} {y} {s} {d[x][y]} {table[x][y]}\n')

    return d[x][y]

if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
