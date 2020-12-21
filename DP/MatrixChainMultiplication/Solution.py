


# matrix chain multiplication

def matrixChain(p, i, j):    
    if i == j:
        return 0
    res = float('inf')

    for k in range(i, j):
        count = matrixChain(p,i,k) + matrixChain(p,k + 1,j) + p[i - 1] * p[k] * p[j]
        print(i,j,count)
        res = min(res, count)

    return res   

p = [40, 20, 30, 10, 30]
i, j = 1, len(p) - 1 



res = matrixChain(p,i,j)
print(res)
