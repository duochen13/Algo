
"""
1. dp(i, j) = longest common continuous subarrat kebftg between A[i:] and B[j:]

2. dp[m][n] = 0, for all j, dp[m][j] = 0; for all i, dp[i][n] = 0

3. if A[i] = B[j]:
    dp(i, j) = dp[i + 1][j + 1] + 1


ex: 
     0 1 2 3 4
A = [1,2,8,2,1]
B = [8,2,1,4,7]

    8  2  1  4  7
1         1        0
2      1           0
8   3              0
2      2           0
1   0  0  1  0  0  0
    0  0  0  0  0  0

"""

def longestCommonContinousSubarray(A, B):
    m, n = len(A), len(B)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    resLen = 0
    resStr = []
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                # print("i: {}, j: {}, dp: {}".format(i, j, dp[i][j]))
                if dp[i][j] > resLen:
                    resLen = dp[i][j]
                    resStr = A[i:i + dp[i][j]]
    return resStr


# //        intput:
A = ["3234.html", "xys.html", "7hsaa.html"]
B = ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]

res = longestCommonContinousSubarray(A, B)
print(res)