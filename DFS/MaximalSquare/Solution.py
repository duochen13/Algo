"""
Input: matrix = 
[["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]]
Output: 4

Input matrix = 
[["1","1","0","1"],
 ["1","1","1","1"],
 ["0","1","1","1"],
 ["0","1","1","1"]]
output: 9

"""

# BFS
# This question is very similiar to 694(Number of Distinct Islands)
def maximalSquare(grid):
   
   if not grid or not grid[0]:
       return 0
   
   m, n = len(grid), len(grid[0])
   res, level = 0, 1
   
   for i in range(m):
       for j in range(n):
           if grid[i][j] == "0":
               continue
   
           q = [(i,j)]
           while q:
               N = len(q)
               # bfs on current level
               for _ in range(N):
                   x, y = q.pop(0)
                   # visited node || water
                   if grid[x][y] != "1":
                       continue
                   # print("({},{}), level:{}".format(x, y, level))
                   # add neighbors to bottom right
                   for a, b in [[0,1], [1,0], [1,1]]:
                       i, j = x + a, y + b
                       # invalid neighbors
                       if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                           res = max(res, level)
                           level = 0
                           break
                       q.append((i, j))
               level += 1     

   return res * res

# DP: 
# f(i,j) = max area of the matrix where its bottomright node locates in (i,j)
# f(i + 1, j + 1) = min(f(i, j + 1), f(i + 1, j), f(i, j)) + 1
def maximalSquare(grid):
    
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    res = 0
    
    dp = [[1 if (i < m and j < n and grid[i][j] == "1") else 0 for i in range(n + 1)] for j in range(m + 1)]
    
    for i in range(1, m):
        for j in range(n):
            if grid[i][j] == "0":
                dp[i][j] = 0
                continue
            res = max(res, 1)
            dp[i + 1][j + 1] = 1 + min(dp[i][j], dp[i + 1][j], dp[i][j + 1])
            res = max(res, dp[i + 1][j + 1])
    
    # print("dp:{}".format(dp))
    
    return res * res


