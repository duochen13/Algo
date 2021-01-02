"""
Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
Return the longest possible length of a word chain with words chosen from the given list of words.


Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca"
"""
import collections

def longestStrChain(words):
    res = float('-inf')
    memo = collections.defaultdict(int)

    words = sorted(words, key=lambda x : len(x))

    for word in words:
        for i in range(len(word)):
            tmp = word[:i] + word[i+1:]
            memo[word] = max(memo[word], 1 + memo[tmp])
            res = max(res, memo[word])
            print("tmp={}, memo[{}]={}".format(tmp, word, memo[word]))

    return res

# assert longestStrChain(words=["a","b","ba","bca","bda","bdca"]) == 4
assert longestStrChain(words=["xbc", "pcxbcf","xb","cxbc","pcxbc"]) == 5
"""
memo = {
    a: 1
    b: 1
    ab: 2
    bca: 3  (memo[ba] + 1)
}

"""


