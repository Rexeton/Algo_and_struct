from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    i = 0
    di={}
    for n in nums:
        if target-n in di:
            return [i,di[target-n]]
        di[n]=i
        i = i + 1


# print(two_sum([2,4,3],6))