from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    i = 0
    l = -1
    for n in nums:
        if target - n == n:
            l = i
        elif target - n in nums:
            l = i
            break
        i = i + 1
    return [l, nums.index(target - nums[l])]
