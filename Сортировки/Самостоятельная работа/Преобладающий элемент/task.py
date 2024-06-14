from typing import List


def majority_element(nums: List[int]) -> int:

    le = len(nums)
    if le==0:
        return None

    di = {}
    max_el = nums[0]
    for el in nums:
        if el in di:
            di[el] += 1
            if di[el] > le / 2:
                max_el = el
                break
        else:
            di[el] = 1
    return max_el
    # return sorted(nums)[le//2]
