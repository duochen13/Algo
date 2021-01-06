
"""
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

def dfs(self, memo, node, res):
    while node in memo and memo[node]:
        self.dfs(memo, memo[node].pop(0), res)
    res.append(node)
    

def findItinerary(self, tickets):
    
    # construct adjacent list for graph representation
    memo = collections.defaultdict(list)
    for departure, arrival in tickets:
        memo[departure].append(arrival)
    # print("before sort:{}".format(memo))
        
    # sort tickets
    for airpot, arrivals in memo.items():
        memo[airpot] = sorted(arrivals)
    print("after sort:{}".format(memo))
        
    # dfs
    curPath = []
    self.dfs(memo, "JFK", curPath) 
    return curPath[::-1]

