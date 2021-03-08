"""
1. dp(i): length of increasing subarray in A[:i]

2. dp(0) = 0

3. for A[i:j], if A[i] < A[j]:
   dp[i] = max(dp[i], dp[j] + 1)


ex:       0  1   2  3   4   5   6   7   8
 i   j   10  22  9  33  21  50  41  60  80
[..] 1    0   1 [10]
     2    0   1  0
     3    0   1  0   2 [10, 22]
     4    0   1  0   2  1
     5    0   1  0   2  1   3 [10, 22, 33]
     6    0   1  0   2  1   3   3
     7    0   1  0   2  1   3   3   4 [10, 22, 33, 50]
     8    0   1  0   2  1   3   3   4   5 [10, 22, 33, 50, 60]

res: [10,22,33,50,60,80] 
"""
import collections


# O(n^2), or O(nlogn) if sort
def LISOnSingleList(nums):
    N = len(nums)
    dp = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return dp[-1]


assert LISOnSingleList(nums=[4,2,3,7,1,10]) == 4
assert LISOnSingleList(nums=[10,22,9,33,21,50,41,60,80]) == 6


