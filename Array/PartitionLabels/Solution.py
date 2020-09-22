
"""
A string S of lowercase English letters is given. We want to partition this string into [as many parts] as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

"ababcbaca defegde hijhklij" 
abc        defg    hijk

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 22
a b a b c b a c a d e  f  e  g  d  e  h  i  j   h  k  l  i j
                                   i
                                   r
                l
memo:
a: 8
b: 5
c: 7
d: 9
e: 10

"""

def partitionLabels(s):
    memo = {c : i for i, c in enumerate(s)}
    r = l = 0
    res = []
    for i, x in enumerate(s):
        r = max(r, memo[x])
        if i == r:
            res.append(r - l + 1)
            l = i + 1
    return res


if __name__ == '__main__':
    res =partitionLabels(s="ababcbacadefegdehijhklij")
    print(res)