"""
You are given a list of strings words from the dictionary, where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language, and return it. If the given input is invalid, return "". If there are multiple valid solutions, return any of them.

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Input: words = ["z","x","z"]
Output: ""

# ["wer","wef","wrt","wrf","er","ett","rftt"]
# ["zy", "zx"]
"""

def alienOrderWrong(words):
    # construct adjacent list and detect cycles if exist
    hashset = collections.defaultdict(set)
    memo = collections.defaultdict(list)
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        if word1 == word2:
            continue
        # detect cycles
        if word1 in hashset[word2]:
            return ""
        k = 0
        while k < min(len(word1), len(word2)) and word1[k] == word2[k]:
            k += 1
        memo[word1[k]].append(word2[k])
        hashset[word1[k]].add(word2[k])
    
    print("hashseT:{}".format(hashset))
    print("memo:{}".format(memo))
    visited = set()
    q = [words[0][0]]
    curPath = ""
    while q:
        curNode = q.pop(0)
        if curNode in visited:
            continue
        curPath += curNode
        # print("curNode:{}, curPath:{}, q:{}".format(curNode, curPath, q))
        visited.add(curNode)
        for node in memo[curNode]:
            if not node in visited:
                q.append(node)
    
    return curPath

