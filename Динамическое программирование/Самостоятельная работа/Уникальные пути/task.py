from functools import lru_cache
def unique_paths(m: int, n: int) -> int:
    ...
    if m==0 or n==0:
        return 0
    if m==1 or n==1:
        return 1
    @lru_cache()
    def req(x, y, m, n):
        if x>m or y>n:
            return 0
        if (x==m and y==n):
            return 1

        return req(x+1,y,m,n)+req(x,y+1,m,n)

    return req(0,0,m-1,n-1)

print(unique_paths(23,12))
