import collections

#  A = 1 0 0 0 1 0 1, S = 2
#      ^
# memo: 0:1, 
# tmp:  1
# res: 0



def numSubarraysWithSum(A, S):
    res = tmp = 0
    memo = collections.defaultdict(int)
    memo[0] = 1
    for r, x in enumerate(A):
        tmp += x
        if (tmp - S) in memo:
            res += memo[tmp - S]
        memo[tmp] += 1
    return res


A = [1,0,1,0,1]
A = [1,0,0,1,0,1]
A = [0,0,0,0,0]
S = 0

res = numSubarraysWithSum(A, S)

print(res)
