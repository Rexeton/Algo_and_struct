from typing import List


def reverse_string(s: List[str]) -> None:
    ...
    le=len(s)-1
    for i in range(le//2):
        s[i],s[le-i]=s[le-i],s[i]
    return s