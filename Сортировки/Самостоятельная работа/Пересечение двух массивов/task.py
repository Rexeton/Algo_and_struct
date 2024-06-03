from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    di = {}
    if len(nums1) > len(nums2):
        for el in nums2:
            if el in nums1 and el not in di:
                di[el] = 1
    else:
        for el in nums1:
            if el in nums2 and el not in di:
                di[el] = 1
    return list(di.keys())


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersection(nums1, nums2)
print(result)