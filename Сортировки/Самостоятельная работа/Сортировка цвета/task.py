from typing import List


def sort_сolors(nums: List[int]) -> None:
    """
    Ничего не возвращайте, вместо этого измените nums на месте.
    """


    if len(nums)==1:
        return nums
    if len(nums)==2:
        if nums[0]>nums[1]:
            nums[0],nums[1]=nums[1],nums[0]
        return nums
    i_min=0
    i_max=len(nums)-1
    i=0
    for _ in range(len(nums)):
        if nums[i] == 0:
            nums[i], nums[i_min] = nums[i_min], nums[i]
            i_min += 1
        if nums[i_max] == 2:
            i_max -= 1
        i+=1
    i=i_min
    for _ in range(i_max-i_min):

        if nums[i] == 2:
            nums[i], nums[i_max] = nums[i_max], nums[i]
            i_max -= 1
        i+=1
        if nums[i_max] == 2:
            i_max -= 1
        if i_max <= i:
            break
    return nums


print(sort_сolors([1,2,2,1,2,0]))
print(sort_сolors([1,2,2,2,2,0,0,0,1,1]))
print(sort_сolors([2,1,2]))
print(sort_сolors( [2,0,2,1,1,0]))
print(sort_сolors([2,1,1]))
print(sort_сolors([0,1,2]))
# print(sort_сolors([2,1,1]))
# print(sort_сolors([1,0,2]))
# print(sort_сolors([2,1]))
# print(sort_сolors([1,2]))
# print(sort_сolors( [1, 2, 0]))
# print(sort_сolors([1,0,1]))
# print(sort_сolors([2,0]))
# print(sort_сolors( [2, 2, 2, 1, 1, 0, 0, 0]))
# print(sort_сolors([2,0,1]))


