"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0. 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0
"""

#Recursion
def LCSRecursion(a, b):
    def LCS(a, b, i, j):
        # base case: LCS("", "abc") = 0
        if not i or not j:
            return 0
        # sub problems
        if a[i] == b[j]:
            return LCS(a, b, i - 1, j - 1) + 1
        return max(LCS(a, b, i - 1, j), LCS(a, b, i, j - 1))
    return LCS(a, b, len(a) - 1, len(b) - 1) + 1


# BottomUp
def LCSBottomUp(a, b):
    m, n = len(a) - 1, len(b) - 1
    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                memo[i + 1][j + 1] = 1 + memo[i][j]
            else:
                memo[i + 1][j + 1] = max(memo[i][j + 1], memo[i + 1][j])
    return memo[m][n]
    

# print(LCSRecursion(a="abcfegikz",b="bacefegk"))
# assert LCSBottomUp(a="abcfegikz",b="bacefegk") == 6


def LCCS(nums1, nums2):
    m, n = len(nums1), len(nums2)
    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    res = 0
    for i in range(m):
        for j in range(n):
            if nums1[i] == nums2[j]:
                memo[i + 1][j + 1] = 1 + memo[i][j]
                res = max(res, memo[i + 1][j + 1])
    return res

assert LCCS(nums1=[1,2,8,2,1], nums2=[8,2,1,4,7]) == 3

"""
a b c f e g j k z
 
b a c e f e g k

output: 3, fegk


f[i,j]: LCS between a[:i] and b[:j]
base case: f[0, x] or f[x, 0] = 0
subproblem: if a[i] == b[j]: f[i, j] = 1 + f[i - 1, j - 1]
            else:            f[i, j] = max(f[i - 1, j], f[i, j - 1])

relation: if a[i + p] == b[j + q], f[i + p,j + q] = f[i,j] + 1, where p, q > 0
result: f[len(a), len(b)]
"""

