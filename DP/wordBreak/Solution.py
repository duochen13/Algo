"""
dp[i]: s[:i] is work break ?

dp[0] = True

dp[j] = dp[i]   if A[i:j] in memo
      = False   else


01234567
leetcode

    0   1   2   3   4   5  6  7  8
dp  T   F   F   F   T            T
 j
 1,2,3     
 4                  T
 5,6,7
 8                               T

ex:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
"""


def wordBreak139(self, s: str, wordDict: List[str]) -> bool:
    
    memo = set(wordDict)
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    for j in range(len(dp)):
        for i in range(j):
            tmp = s[i:j]
            if tmp in memo and dp[i]:
                dp[j] = True
    
    return dp[-1]


"""
dp[i]: A[:i] is word break able

dp[0] = True

dp[j] = dp[i] if A[i:j] in memo


   0 1 2 3 4 5 6 7 8 9
   c a t s a n d d o g

dp  T F F [""]
         T ["cat"] 
           T F F ["cats"]
                 T F F  ["cat sand", "cats and"]
                       T ["cat sand dog", "cat sand dog"]
"""


def wordBreak140(s, wordDict)
    
    memo = set(wordDict)
    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True
    strs = {i : [] for i in range(len(s) + 1)}
    strs[0] = [""]
    for j in range(len(dp)):
        for i in range(j):
            tmp = s[i:j]
            if dp[i] and tmp in memo:
                dp[j] = True
                for prefix in strs[i]:
                    strs[j].append((prefix + " " if prefix != "" else "") + tmp)
                    # print("prefix: {}, i:{} j: {}, tmp:{}, str[j]: {}".format(prefix, i, j, tmp, strs[j]))
    return [x for x in strs[len(dp) - 1]]
    
        