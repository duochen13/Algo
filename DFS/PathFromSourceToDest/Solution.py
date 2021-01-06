"""
ref :https://leetcode.com/problems/all-paths-from-source-lead-to-destination/
"""

def dfs(memo, visited, node, destination):
    # leaf node detected, make sure leaf node is destination
    if not memo[node]:
        return node == destination
    # detect cycles
    if visited[node] != 0:
        return visited[node] == 2
    # mark current node as visiting
    visited[node] = 1
    # dfs
    for n in memo[node]:
        if not dfs(memo, visited, n, destination):
            return False
    return True


def leagsToDestination(n, edges, source, destination):
    # construct adjacent list for graph representation
    memo = collections.defaultdict(list)
    for a, b in edges:
        memo[a].append(b)
    # construct state hashtable, { 0:unvisted, 1:visiting, 2:visited}
    visited = { node : 0 for node in range(n) }

    return dfs(memo, visited, source, destination)

