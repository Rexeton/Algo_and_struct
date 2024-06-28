from typing import Union

import networkx as nx
from  matplotlib import pyplot

def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы

    res= nx.dijkstra_predecessor_and_distance(graph,0)
    return res[1][len(res[1])-1]
if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    ...  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    stairway_graph =nx.DiGraph()
    stairway_graph.add_weighted_edges_from([(i,i+1,stairway[i]) for i in range(len(stairway))]+\
       [(i,i+2,stairway[i+1]) for i in range(len(stairway)-1)])
    # nx.draw_networkx(stairway_graph,node_color='green',node_size=1000,with_labels=True)
    # pyplot.show()
    print(stairway_path(stairway_graph))  # 72