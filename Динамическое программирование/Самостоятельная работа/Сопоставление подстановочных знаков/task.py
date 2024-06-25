def is_match(s: str, p: str) -> bool:
    ...
    ls=len(s)
    lp=len(p)
    i=0
    j=0
    while j<lp:
        if p[j]=='?':
            i+=1
            j+=1
        if p[j]=='*':
            while i<ls-1:
                if p[j+1]!=s[i]:
                    i+=1
                else:
                    break
            while i < ls-1:
                if p[j ] == s[i]:
                    i += 1
                else:
                    break
            i+=1
            j+=1
            continue
        if p[j]!=s[i]:
            return False
        else:
            i+=1
            j+=1
    return i==ls

print(is_match("aa", "a"), False)
print(is_match("aa", "a*"), True)
print(is_match("mississippi", "m??*ss*?i*pi"), False)
print(is_match("ab", ".*"), False)
print(is_match("aab", "c*a*b"), False)
# print(is_match("aa", "a"), False)