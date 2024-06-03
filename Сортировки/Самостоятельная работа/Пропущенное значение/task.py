from typing import List


def missing_number(nums: List[int]) -> int:
    list2=[-1]*(len(nums)+1)
    for el in nums:
        list2[el]=el
    for i in range(len(list2)):
        if list2[i]==-1:
            return i
a=0
print(missing_number([3,0,1]))