from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    di = {}
    res = {}
    res2 = []
    nums = nums
    for el in nums:
        if el in di:
            if el == 0:
                di[el] += 1
            else:
                di[el] = 2
        else:
            di[el] = 1
    if di.get(0):
        if di[0] > 2:
            res2.append([0, 0, 0])
            di[0] = 1
    di2 = di.copy()
    for el in di:
        while di2.get(el):
            di2[el] -= 1
            if di2[el] <= 0:
                di2.pop(el)
            for el2 in di2:
                need = -(el + el2)
                di2[el2] -= 1
                if di2.get(need):
                    if di2[need] > 0:
                        mm = sorted([el, el2, need])
                        s = ''
                        for st in mm:
                            s += str(st) + '!'
                        if res.get(s) != 0:
                            res[s] = 0
                            res2.append(mm)
                di2[el2] += 1
    return res2
