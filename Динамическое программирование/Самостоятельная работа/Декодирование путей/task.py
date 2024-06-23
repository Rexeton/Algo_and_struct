def num_decodings(s: str) -> int:
    ...
    d={str(i) for i in range(1,27)}
    def req(s):
        i=1
        while i<len(s):
            if f'{s[i-1]}{s[i]}' not in d:
                return req(s[:i])*req(s[i:])
            i+=1
        if len(s)==0:
            return 1
        if len(1)==1:
            if s[0] in d:
                return 1
            return 0


    return req(s)

print(num_decodings("11106"))