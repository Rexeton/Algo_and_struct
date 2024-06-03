def is_anagram(s: str, t: str) -> bool:
    di={}
    if len(s) != len(t):
        return False
    for el in s:
        if el in di:
            di[el]+=1
        else:
            di[el]=1
    for el in t:
        if el in di:
            di[el]-=1
        else:
            return False
    return max(di.values())==0

print(is_anagram('anagram','nagaram'))