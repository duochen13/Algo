"""
input: N=4, nodes=[[1,2], [1,3], [2,1],[3,4]]
output: true

input: N=5, nodes=[[1,3],[1,2],[2,5],[5,4]]
output: true

input: N=5, nodes=[[1,2],[2,3],[3,4],[4,5],[1,5]]
output: false

input: N=4, nodes=[[1,2],[3,4]]
output: 
"""
import collections

def dfs(node, memo, set1, set2, skip):
    print("node:{}, set1:{}, set2:{}".format(node, set1, set2))
    # base case
    if skip:
        if node in set2:
            return False
        if node in set1:
            return True
        set1.add(node)
    else:
        if node in set1:
            return False
        if node in set2:
            return True
        set2.add(node)
    # flip skip
    skip = not skip
    # dfs
    for n in memo[node]:
        if not dfs(n, memo, set1, set2, skip):
            return False
    return True



def ableToDivideRur(N, nodes):
    # construct adijacent list for graph representation
    memo = collections.defaultdict(list)
    for a,b in nodes:
        memo[a].append(b)
        memo[b].append(a)
    print("memo:{}".format(memo))
    # initialize hash set when dfs
    set1, set2 = set(), set()
    for n, _ in nodes:
        if not dfs(n, memo, set1, set2, True):
            return False
    return True


def ableToDivide(N, nodes):
    memo = collections.defaultdict(list)
    for a, b in nodes:
        memo[a].append(b)
        memo[b].append(a)
    skip = True
    set1, set2 = set(), set()
    stack = [1]
    while stack:
        node = stack.pop()
        # base case
        if skip:
            if node in set2:
                return False
            if node in set1:
                return True
            set1.add(node)
        else:
            if node in set1:
                return False
            if node in set2:
                return True
            set2.add(node)
        # dfs
        skip = not skip
        for n in memo[node]:
            stack.append(n)
    return True







# assert ableToDivide(N=4,  nodes=[[1,2], [1,3], [2,1],[3,4]]) == True
# assert ableToDivide(N=5,  nodes=[[1,3], [1,2], [2,5],[5,4]]) == True
# assert ableToDivide(N=5, nodes=[[1,2],[2,3],[3,4],[4,5],[5,1]]) == False
assert ableToDivide(N=4, nodes=[[1,2],[3,4]]) == True

"""
input: N=4, nodes=[[1,2],[3,4]]
output: true
"""
    




