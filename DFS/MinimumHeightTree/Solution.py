"""
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]

Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
"""

import collections

def dfs(memo, node, parent, depth):
    # leaf node
    if len(memo[node]) == 1 and memo[node][0] == parent:
        return depth
    # dfs
    tmp = 0
    for n in memo[node]:
        if n != parent:
            tmp = max(tmp, dfs(memo, n, node, depth + 1))
    return tmp


def findMinHeightTrees(n, edges):
    # construct adjacent list for graph representation
    memo = collections.defaultdict(list)
    for a, b in edges:
        memo[a].append(b)
        memo[b].append(a)
    
    mapping = collections.defaultdict(list)
    minDist = float('inf')

    for node in range(n):
        dist = dfs(memo, node, parent=-1, depth=0)
        minDist = min(minDist, dist)
        mapping[dist].append(node)
        print("node:{}, dist:{}".format(node, dist))

    return mapping[minDist]


assert findMinHeightTrees(n=4, edges=[[1,0],[1,2],[1,3]]) == [1]



