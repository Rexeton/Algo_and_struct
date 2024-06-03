from typing import List


def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    """
    for el in nums:
        di[el]+=1
    res=[]
    for el in di:
        res+=[el]*di[el]
    nums=res

print(sort_сolors([2,0,2,1,1,0]))