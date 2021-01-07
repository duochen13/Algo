"""
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "ac"
Output: "a"

Input: s = "cabadc"
Output: "aba" (why you need bool 2d matrix)
"""

"""
1. f(i, j): LPS in s[i:j] (inclusive, opps not in py!)
2. f(k, k) = 1
3. if s[i] == s[j] && s[i - 1:j + 1] is palindromic!!!!
       f(i, j) = 2 + f(i + 1, j -1)
   else:
       f(i, j) = max(f(i,j - 1), f(i + 1, j))
"""

def longestPalindrome(self, s):
   if not s or len(s) == 1:
       return s
     
   N = len(s)
   dp = [[(0 if i != j else 1) for i in range(N + 1)] for j in range(N + 1)]
   table = [[(True if i >= j else False) for j in range(N + 1)] for i in range(N + 1)]
 
   i, j, k = 0, 1, 1
   resLen, resStart, resEnd = 1, 0, 0
   while True:
       # reset i and j
       if j == N:
           i = 0
           k += 1
           j = k
       if i == 0 and j == N:
           break
       # print("i:{},j:{},k:{}".format(i,j,k))
       if s[i] == s[j] and table[i + 1][j - 1]:
           dp[i][j] = 2 + dp[i + 1][j - 1]
           table[i][j] = True
       else:
           dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
       # update resLen and resStr
       if dp[i][j] > resLen:
           resLen = dp[i][j]
           resStart = i
           resEnd = j
       i += 1
       j += 1
   
   return s[resStart:resEnd + 1]



