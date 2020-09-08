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

def longestIncreasingSubsequence(nums):
    dp = [1 for _ in range(len(nums) + 1)]
    memo = [[num] for num in nums]
    res = 1
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] < nums[j]:
                # dp[j] = max(dp[j], dp[i] + 1)
                if dp[i] + 1 > dp[j]:
                    memo[j] = memo[i] + [nums[j]]
                    dp[j] = dp[i] + 1
                res = max(res, dp[j])
    # print(memo)
    return res


res = longestIncreasingSubsequence(nums=[10,22,9,33,21,50,41,60,80])
# print(res)