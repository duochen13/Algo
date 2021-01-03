"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
"""

import collections

def dfs(memo, visited, node, parent):
    # visited, cycle detected
    if node in visited:
        return False
    # mark as visited
    visited.add(node)
    # dfs
    for n in memo[node]:
        if n != parent:
            if not dfs(memo, visited, n, node):
                return False
    return True

def validTree(n, edges):
    # construct adjacent list for graph representation
    memo = collections.defaultdict(list)
    for start, end in edges:
        memo[start].append(end)
        memo[end].append(start)
    # hashset to store visited nodes
    visited = set()
    # check if there is a cycle through dfs, starting from node 0
    if not dfs(memo, visited, 0, -1):
        return False
    # check if graph is connected
    return len(visited) == n




