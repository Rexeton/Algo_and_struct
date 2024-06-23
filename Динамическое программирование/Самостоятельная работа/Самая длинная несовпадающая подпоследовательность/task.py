from typing import List
from functools import lru_cache

def is_subsequence(s: str, t: str) -> bool:
    ...
    i=0
    j=0
    ls=len(s)
    lt=len(t)


    if len(s)==0:
        return 1
    while i<lt:
        if t[i]==s[j]:
            j+=1
        if j==ls:
            return 1
        i+=1
    return 0



def find_lus_length(strs: List[str]) -> int:
    ...
    s=list(sorted(strs,key=len,reverse=True))
    for i in range(1,len(s)):
        if is_subsequence(s[i],s[i-1])==0:
            return len(s[i])
    return -1
s=  ["aabbcc", "aabbcc","bc","bcc","aabbccc"]
print(find_lus_length(s))


def findLUSlength(strs: List[str]) -> int:
    ss = list(sorted(strs, key=len, reverse=True))
    for i in range(1, len(ss)):
        b = 0
        s = ss[i]
        t = ss[i-1]
        ls = len(s)
        lt = len(t)
        if len(s) == 0:
            b = 1
        ii = 0
        j = 0
        while ii < lt:
            if t[ii] == s[j]:
                j += 1
            if j == ls:
                b = 1
                break
            ii += 1

        if b == 0:
            return len(ss[i])
    return -1


print(findLUSlength(s))