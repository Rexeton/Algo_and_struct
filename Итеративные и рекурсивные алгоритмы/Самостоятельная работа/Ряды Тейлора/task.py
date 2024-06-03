from typing import Union
from itertools import count
from math import factorial


DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    ...  # TODO вычислить sin(x) с помощью разложения сумму бесконечного ряда
    sum=x
    n=1
    while True:
        new_el=((-1)**(n)/factorial(2*n+1))*x**(2*n+1)
        if abs(new_el)>DELTA:
            sum+=new_el
            n+=1
        else:
            break
    return sum
a=0
print(sinx(1.55433))