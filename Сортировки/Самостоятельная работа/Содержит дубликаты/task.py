from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    return not len(set(nums))==len(nums)
