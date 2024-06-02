"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self._queue=[]  # TODO инициализировать список


    def enqueue(self, elem: Any) -> None:  # O(n)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._queue.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any: #O(n)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """

        ...# TODO реализовать метод dequeue
        if not self._queue:
            IndexError
        first_elem=self._queue[0]
        if len(self._queue)==1:
            self._queue = []
        else:
            self._queue=self._queue[1:]
        return first_elem

    def peek(self, ind: int = 0) -> Any: #O(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind,int):
            raise TypeError
        if ind<0 or ind>len(self._queue):
            raise IndexError
        return self._queue[ind]  # TODO реализовать метод peek

    def clear(self) -> None: #O(1)
        """ Очистка очереди. """
        ...  # TODO реализовать метод clear
        self._queue=[]

    def __len__(self): #O(1)
        """ Количество элементов в очереди. """
        ...  # TODO реализовать метод __len__
        return self._queue.__len__()

