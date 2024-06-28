from typing import Hashable, List
from collections import deque

import networkx as nx
from  matplotlib import pyplot

def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в ширину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в ширину
    res=[]
    qu_=[start_node]
    visit=set()
    visit.add(start_node)
    while qu_:
        visited_node=qu_.pop(0)
        res.append(visited_node)
        for elem in g[visited_node]:
            if elem not in visit:
                qu_.append(elem)
                visit.add(elem)

    return res
if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    g=nx.Graph()
    g.add_nodes_from('ABCDEFGHJ')
    g.add_edges_from(
        [('A','B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('H', 'J'),
        ('H', 'E'),
        ('H', 'D'),
         ('H', 'C'),
         ('H', 'I'),
        ('D', 'E')]
    )
    print(bfs(g,'A'))
    # nx.draw_spring(g,node_color='green',node_size=1000,with_labels=True)
    # pyplot.show()