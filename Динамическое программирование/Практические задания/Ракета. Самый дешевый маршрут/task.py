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
    requrc(0, 0, n-1, m-1, d, table,0)
    return d

def requrc(x,y,n,m,d,table,s):
    if (x>n or y>m):
        return 0
    if d[x][y]=='!':
        d[x][y]=s+table[x][y]
    if (x==n and y==m):
        d[x][y]=min(d[x][y],s+table[x][y])

    d[x][y]=min(d[x][y],s+table[x][y])
    b=requrc(x + 1, y, n, m, d, table, d[x][y]) + requrc(x, y + 1, n, m, d, table, d[x][y])
    for i in range(n+1):
        print([d[i][j] for j in range(m+1)])
    print('\n')
    return 0

if __name__ == '__main__':
    coasts_ceil = [
        [2, 7, 9, 3],
        [12, 4, 1, 9],
        [1, 5, 2, 5]
    ]
    total_coasts = rocket_coasts(coasts_ceil)
    print(total_coasts[-1][-1])  # 21
