from typing import List


def trap(height: List[int]) -> int:
    ...
    sum=0
    lh=len(height)
    set_h=sorted(set(height))
    j=1
    while j<len(set_h):
        nach=0
        prom_sum=0
        koef = set_h[j] - set_h[j-1]
        for i in range(0,lh):
            if height[i]>=set_h[j]:
                nach=1
            if set_h[j]<=height[i]:
                sum+=prom_sum*koef
                prom_sum=0
            if set_h[j]-height[i]>0:
                prom_sum+=1*nach
        j+=1
    return sum

print(trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]), 23)
print(trap([4,2,0,3,2,5]),9)
print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
print(trap([4, 2, 0, 3, 2, 4, 3, 4]), 10)
print(trap([2, 0, 2]), 2)
print(trap([3, 0, 0, 2, 0, 4]), 10)
