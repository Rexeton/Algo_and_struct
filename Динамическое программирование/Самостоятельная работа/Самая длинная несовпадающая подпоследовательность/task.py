from typing import List


def is_subsequence(s: str, t: str) -> bool:
    ...
    i=0
    j=0
    ls=len(s)
    lt=len(t)


    if len(s)==0:
        return True
    while i<lt:
        if t[i]==s[j]:
            j+=1
        if j==ls:
            return True
        i+=1
    return False



def find_lus_length(strs: List[str]) -> int:
    ...



