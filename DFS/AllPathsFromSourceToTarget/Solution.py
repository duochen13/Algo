"""
Given a directed acyclic graph of N nodes. Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Input: graph = [[1],[]]
Output: [[0,1]]


Asumption: Some nodes can be ioslated, and node should be with in the range of len()
[[1,3],[],[4]]
output: [[0,1],[0,3],[2,4]]

Assumption: We can return in any order


General idea: 
travse all nodes, find all path starting from current nodes

Need a hsahtable called 'visited' to keep track of the visited nodes.
Need a 'prePath' list to preserve the previous visited nodes in the path

When we reach a node that does not have any out egdes, we add curPath to res

"""

# 1. 2^n path between node 0 and node n 
def dfs(graph, prePath, curNode, res):
    # if curNode does not have any endNode, we arrive the destination
    if curNode == len(graph) - 1:
        prePath.append(curNode)
        res.append(prePath)
        return
    # keep searching, treat the endNode as the curNode in the next search
    for endNode in graph[curNode]:
        dfs(graph, prePath + [curNode], endNode, res)


def findAllPaths(graph):
    res, prePath = [], []
    curNode = 0

    dfs(graph, prePath, curNode, res)

    return res

# 2.
def findAllPathsIt(graph):
    stack, res = [(0, [0])], []

    while stack:
        curNode, curPath = stack.pop()
        if curNode == len(graph) - 1:
            res.append(curPath)
            assert not graph[curNode]
        for nextNode in graph[curNode]:
            stack.append((nextNode, curPath + [curNode]))

    return res


"""
           0    1   2   3
graph = [[1,2],[3],[3],[]]

visited = {0:T, 1:T, 2:T, 3:F}
res = [[0,1,3], [0,2,3]]

dfs(prePath=[], curNode=0)
|                             \
dfs(prePath=[0], curNode=1)      dfs(prePath=[0], curNode=2)
|                                       \
dfs(prePath=[0,1], curNode=3)         dfs(prePath=[0,2], curNode=3)
|                                         \
prePath=[0,1,3]                          prePath=[0,2,3]


Output: [[0,1,3],[0,2,3]]

           0       1      2   3   4
graph = [[4,3,1],[3,2,4],[3],[4],[]]

visited = {0:T, 1:T, 2:F, 3:T, 4:F}
res = []

dfs(prePath=[], curNode=0)
        |                           
dfs(prePath=[0], curNode=4)    dfs(prePath=[0], curNode=3)      dfs(prePath=[0], curNode=1)

prePath=[0, 4]                 dfs(prePath=[0,3], curNode=4)    dfs(prePath=[0,1], curNode=3)   dfs(prePath=[0,1], curNode=2)  dfs(prePath=[0,1], curNode=4)

                               prePath=[0,3,4]                  dfs(prePath=[0,1,3])
"""

