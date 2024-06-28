from typing import Hashable, List
from collections import deque

import networkx as nx
from  matplotlib import pyplot

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в глубину итеративным способом
    deq=[start_node]
    visit = set()
    res = []
    while deq:
        v_node=deq.pop(0)
        visit.add(v_node)
        res.append(v_node)
        for elem in g[v_node]:
            if elem not in visit:
                deq.insert(0,elem)
    return res
if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    g=nx.Graph()
    g.add_nodes_from('ABCDEFG')
    g.add_edges_from(
        [('A','B'),
        ('A', 'C'),
        ('B', 'E'),
        ('F', 'C'),
        ('G', 'E'),
        ('B', 'D')]
    )
    print(dfs(g,'A'))
    nx.draw_spring(g,node_color='green',node_size=1000,with_labels=True)
    pyplot.show()