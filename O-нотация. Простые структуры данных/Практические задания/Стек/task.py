from typing import Any


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, elem: Any) -> None:
        """
        Добавление элемента в вершину стека

        :param elem: Элемент, который должен быть добавлен
        """
        self._stack.append(elem)   # TODO реализовать операцию push

    def pop(self) -> Any:
        """
        Извлечение элемента из вершины стека.

        :raise: IndexError - Ошибка, если стек пуст

        :return: Извлеченный с вершины стека элемент.
        """
        # TODO реализовать операцию pop
        if not self._stack:
            raise IndexError('Error? stack is null')
        return self._stack.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в стеке, без его извлечения.

        :param ind: индекс элемента (отсчет с вершины, 0 - вершина, последний добавленный элемент, 1 - предпоследний элемент, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ стека

        :return: Значение просмотренного элемента
        """
        # TODO реализовать операцию peek
        if not isinstance(ind, int):
            raise TypeError(f'{ind} не число')
        if ind<0 or ind>len(self._stack):
            raise IndexError(f'не существует {ind} элемент')
        return self._stack[-1-ind]


    def clear(self) -> None:
        """ Очистка стека. """
        self._stack.clear()  # TODO реализовать операцию clear


    def __len__(self) -> int:
        """ Количество элементов в стеке. """
        return self._stack.__len__()  # TODO реализовать операцию __len__
