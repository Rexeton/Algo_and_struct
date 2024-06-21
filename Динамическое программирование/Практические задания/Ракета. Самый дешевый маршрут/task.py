from typing import List


def rocket_coasts(table: List[List[int]]) -> List[List[int]]:
    """

    Просчитать минимальные стоимости маршрутов до каждой клетки с учетом возможных перемещений.


    :param table: Таблица размером N*M, где в каждой клетке дана стоимость перемещения в неё
    :return: Таблицу стоимостей перемещения по клеткам
    """
    ...  # TODO рассчитать таблицу стоимостей перемещений
    n = len(table)
    m = len(table[0])
    d = []
    for j in range(n):
        a2 = []
        for i in range(m):
            a2.append('!')
        d.append(a2)
    requrc(0, 0, n-1, m-1, d, table,table[0][0])
    #d[-1][-1]=table[0][0]+d[0][0]
    return d

def requrc(x,y,n,m,d,table,s):
    if (x>n or y>m):
        return 0
    if (x==n and y==m):
        return table[x][y]
    if d[x][y]!='!':
        d[x][y]=min(d[x][y],s)
    if d[x][y]=='!':
        d[x][y]=requrc(x+1,y,n,m,d,table,s)+requrc(x,y+1,n,m,d,table,s)


    print(f'{x} {y} {s}\n')

    return table[x][y]

if __name__ == '__main__':
    coasts_ceil = [
        [2, 7],
        [12, 4]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts[-1][-1])  # 21
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]