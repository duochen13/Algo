'''

You work at a multi-level marketing agency
There is one founder and the founder can recruit up to 2 mentees. 
Each mentee, will then recruit up to two mentees -> mentor / mentee relationship

Each employee, independently, will bring some sort of profit to the company

'''

# Question 1 : design a data structure to represent this company
"""
      founder
       /  \ 
      A     B
      / \     \
     C  D     E
         /
         F 
"""

class Node: 
    def __init__(self, eid, profit, firstMentee, secondMentee):
        self.eid = eid
        self.profit = profit
        self.firstMentee = firstMentee
        self.secondMentee = secondMentee
        
"""
        -10                0(eid)
       /   \        
      9     20           1    2
           /  \
          7    5              3  4 
"""
secondMentee = Node(2, 20, Node(3, 7, None, None), Node(4, 5, None, None))
root = Node(0, -10, Node(1, 9, None, None), secondMentee)


# Question 2 : the company is going thru restructuring, we want to know all the employees at each level
# 0 > 1 == 2 > 3 == 4
# (1) Lists [[0], [1,2], [3,4]]
'''
res = []
q = [-10], level=0, N = len(q) = 1  append current q to res list
append all current level employees's mentee to the queue
q = [9, 20], level=1, N = len(q) = 2 (pop 2 times)
q = [20, A, B]
append 
q = [7, 5], level=2

res = []
q = [-10], N = 1
  res = [[0]]
q = [9, 20], N = 2
  res = [[0], [1,2]]
q = [7, 5], N = 2
  res = [[0], [1,2], [3,4]]


'''

def findEmployeesByLevels(node):
    res, q = [], [node]
    while q:
        N = len(q)
        res.append([node.eid for node in q])
        for _ in range(N):
            curNode = q.pop(0)
            if curNode.firstMentee:
                q.append(curNode.firstMentee)
            if curNode.secondMentee:
                q.append(curNode.secondMentee)
    return res


res = findEmployeesByLevels(root) 
# print(res)

# Question 3 : as a part of the restrucuturing, we want to layoff some employees who are not beneficial to the company 
# You cannot have two separate companies - can only have one
# You have to uphold the tree structure
# The goal is to maximize the profit

"""
        -10                0(eid)
       /   \        
      9     20           1    2
           /  \
          7    5              3  4 
          
            20
            /\
            7  5   
profit = 42    
        
         10                0(eid)
       /   \        
      9     20           1    2
           /  \
          7    5              3  4     
profit = 61

         10                0(eid)
       /   \        
      9    -20           1    2
           /  \
          7    5              3  4    

           profit:10+9
           /      \
     proft:9     profit:-20+7+5=-8     
                      /\
                    7   5

         10                0(eid)
       /   \        
      9    -20           1    2
           /  \
          70   -5              3  4    
        
    (70-20) + 9 + 10 = 69
    
         same level                 upper level
    max ( max( max(-5, 0) + max(70, 0), 0 ) + (-20),  0 )
             0           70                
                    70                       -20
                             50
                             
                             
 globalProfit = float('-inf') 
 globalProfit = max(globalProfit, curProfit) = 70
 
             curProfit
             /        \  
        curProfit      curProfit = max(sum(all child proftis) + curnode's profit, 0) = max((70+0) - 20, 0) = 50
                        /         \     
                  curProfit:70    curProfit = max(sum(all child proftis) + cunode's profit, 0) = max((0 - 20, 0) = 0
                   
        -10                0(eid)
       /   \        
      9     20           1    2
           /  \
          7    5              3  4 
"""

def findMaxProfit(node):
    globalProfit = float('-inf')
    
    def dfs(node, lastProfit):
        nonlocal globalProfit
        if not node:
            return 0
        if not node.firstMentee and not node.secondMentee:
            return max(node.profit, 0)
        # sum of all mentee's profits + current node's profit
        # check if current node is root
        
        curNodeProfit =  max(node.profit, 0)
        curProfit = max(dfs(node.firstMentee) + dfs(node.secondMentee) + curNodeProfit, 0)
        globalProfit = max(globalProfit, curProfit)
        return curProfit
    
    dfs(node, node.profit)
    return globalProfit

res = findMaxProfit(root)
print(res)

