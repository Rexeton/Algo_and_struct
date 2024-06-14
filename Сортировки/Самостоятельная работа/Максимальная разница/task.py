from typing import List


def maximum_gap(nums: List[int]) -> int:
    max_value = 0
    b = sorted(nums)
    for i in range(1, len(nums)):
        max_value = max(max_value, b[i] - b[i - 1])
    return max_value
