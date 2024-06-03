def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # TODO реализовать рекурсивный алгоритм нахождения факториала

    if n<0 :
        raise ValueError
    if not isinstance(n,int):
        raise TypeError
    if n<2:
        return 1
    factorial=n*factorial_recursive(n-1)
    return factorial
