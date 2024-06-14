from typing import List


def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    """
    if len(nums)==1:
        return nums
    min_num = nums[0]
    max_num = nums[0]
    ...
    while c<len(nums):
        if nums[i]!=0:
            nums[i_max], nums[i] = nums[i], nums[i_max]
        else:
            i_min+=1
        c+=1
    return nums


print(sort_сolors([1,2]))
print(sort_сolors([1,0,1]))
print(sort_сolors([2,0]))
print(sort_сolors( [2,0,2,1,1,0]))
print(sort_сolors( [1, 2, 0]))
print(sort_сolors( [2, 2, 2, 1, 1, 0, 0, 0]))
print(sort_сolors([2,0,1]))


