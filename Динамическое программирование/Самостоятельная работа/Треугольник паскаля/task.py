from typing import List


def generate(num_rows: int) -> List[List[int]]:
    ...
    n=num_rows+1
    res=[]
    for i in range(1,n):
        dop=[1 for _ in range(i)]
        for j in range(1,(i//2)):
            el=res[-1][j-1]+res[-1][j]
            dop[j]=el
            dop[-j -1]=el
        if i%2==1 and i>2 :
            col=i//2
            dop[col]=res[-1][col-1]+res[-1][col]
        res.append(dop)

    return res


print(generate(5))