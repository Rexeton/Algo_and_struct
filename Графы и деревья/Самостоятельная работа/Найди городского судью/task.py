from typing import List


def find_judge(n: int, trust: List[List[int]]) -> int:
    ...
    mirn = {}
    judj = {}
    if n == 1:
        return 1
    for el in trust:
        if el[0] in mirn:
            mirn[el[0]] += 1
        else:
            mirn[el[0]] = 0
        if el[1] in mirn:
            return -1
        if el[1] not in judj:
            judj[el[1]] = 1

    if len(judj) != 1:
        return -1
    else:
        for el in judj:
            return el