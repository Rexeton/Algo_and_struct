def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    ...  # TODO написать итеративный алгоритм чисел Фибоначчи
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
    for i in range(2,n+1):
        f=f1+f2
        f1,f2=f2,f
    return f
a=0
print(fib_iterative(5))