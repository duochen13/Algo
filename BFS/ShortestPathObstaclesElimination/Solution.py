"""
Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Input:
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
Output: -1
Explanation:
We need to eliminate at least two obstacles to find such a walk.
"""

def shortestPath(self, grid, K):

   if not grid or not grid[0]:
       return 0
   m, n = len(grid), len(grid[0])

   cnt = 0
   q = [(0,0,K)]
   while q:
       N = len(q)
       for _ in range(N):
           x, y, k = q.pop(0)
           # base case
           if x == m - 1 and y == n - 1:
               return cnt
           # mark current node as visited
           grid[x][y] = -2
           # bfs
           for a, b in [[-1,0],[1,0],[0,-1],[0,1]]:
               i, j = x + a, y + b
               # out of range
               if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -2:
                   continue
               if grid[i][j] == 0:
                   q.append((i, j, k))
               elif grid[i][j] == 1 and k > 0:
                   q.append((i, j, k - 1))
       cnt += 1

   return -1 if grid[m - 1][n - 1] != -2 else cnt
                    
