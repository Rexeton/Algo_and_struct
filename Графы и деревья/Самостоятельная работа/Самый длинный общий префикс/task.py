from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    ...
    if len(strs)==0:
        return ''
    if len(strs)==1:
        return strs[0]
    strs.sort()
    res=''
    for i in range(len(strs[0])):
        if strs[0][i]!=strs[-1][i]:
            return res
        res += strs[0][i]
    return res


print(longest_common_prefix(["dog","racecar","car"]))