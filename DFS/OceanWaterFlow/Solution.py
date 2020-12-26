"""
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
  Pacific ~   ~   ~   ~   ~ 
       ~ (1) (2) (2) (3) (5) 
       ~ (3) (2) (3) (4) (4) 
       ~ (2) (4) (5)  3   1  
       ~ (6) (7)  1   4   5  
       ~ (5)  1   1   2   4  
 
          1   2   2   3  (5) *
          3   2   3  (4) (4) *
          2   4  (5) (3) (1) *
          6  (7) (1) (4) (5) *
         (5) (1) (1) (2) (4) *
          *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

def dfs(matrix, memo, x, y):
    m, n = len(matrix), len(matrix[0])
    memo[x][y] = True
    stack = [[x, y]]
    while stack:
        x, y = stack.pop()
        memo[x][y] = True
        for a, b in [[-1,0],[1,0],[0,-1],[0,1]]:
            if x + a < 0 or x + a >= m or y + b < 0 or y + b >= n or memo[x + a][y + b] or matrix[x + a][y + b] < matrix[x][y]: # out of range of visited
                continue        
            stack.append([x + a, y + b])

def Solution(matrix):
    m, n = len(matrix), len(matrix[0])
    pacific = [[False for _ in range(n)] for _ in range(m)]
    atlantic = [[False for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        dfs(matrix, atlantic, i, n - 1)
        dfs(matrix, pacific, i, 0)
    for j in range(n):
        dfs(matrix, atlantic, n - 1, j)
        dfs(matrix, pacific, 0, j)

    res = []
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                res.append([i,j])

    print(res)

matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

Solution(matrix)

"""
[(0,0)]
[(0,1),(1,0)], [(0,1),(1,1),(2,0)], [(0,1),(1,1),(2,1),(3,0)],  [(0,1),(1,1),(2,1),()

"""
