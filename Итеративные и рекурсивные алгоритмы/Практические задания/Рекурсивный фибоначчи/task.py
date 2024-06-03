def fib_recursive(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя рекурсивный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    ...  # TODO реализовать рекурсивный алгоритм
    f1=0
    f2=1
    if n<0:
        raise ValueError
    if not isinstance(n,int):
        raise TypeError
    if n==0:
        return f1
    if n==1:
        return f2
    f=fib_recursive(n-1)+fib_recursive(n-2)

    return f
