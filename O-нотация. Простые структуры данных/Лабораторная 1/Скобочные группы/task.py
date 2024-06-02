from typing import Any
def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    ...  # TODO реализовать проверку скобочной группы
    if len(brackets_row)%2!=0:
        return False
    # count_of_skobki=0
    # for el in brackets_row:
    #     if el=='(':
    #         count_of_skobki+=1
    #     else:
    #         count_of_skobki -= 1
    #         if count_of_skobki<0:
    #             return False
    # return count_of_skobki==0

    count_of_skobki=Stack()
    for el in brackets_row:
        if el=='(':
            count_of_skobki.push(el)
        else:
            if len(count_of_skobki)==0:
                return False
            count_of_skobki.pop()
    return len(count_of_skobki)==0

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

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False


