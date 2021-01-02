"""
0 1 1 0 0
0 0 1 0 0
0 0 0 1 1
0 0 0 0 1
output: 1 pair of equal matrix

1 1 0 0 
1 1 1 0
0 0 0 0
0 1 1 0
0 1 1 0
output 0 pair of equal matrix
"""

def collectMatrix(grid, diffx, diffy, i, j, memo):
    m, n = len(grid), len(grid[0])
    # out of range or visited or no values
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1 or grid[i][j] == 0:
        return
    # mark cur position as visited
    grid[i][j] = -1
    # dfs
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]
    # store in memo
    memo[-1].append([i - diffx, j - diffy])
    for a, b in dirs:
        collectMatrix(grid, diffx, diffy, i + a, j + b, memo)


def isEqual(grid, matrix1, matrix2):
    if len(matrix1) != len(matrix2):
        return False
    N = len(matrix1)
    for i in range(N):
        x0, y0 = matrix1[i]
        x1, y1 = matrix2[i]
        if x0 != x1 or y0 != y1:
            return False
    return True

def equalMatrix(grid):
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    
    memo = []

    # collect all matrix
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                memo.append([])
                collectMatrix(grid, i, j, i, j, memo)
                print("memo:{}".format(memo))

    # find equal matrix
    cnt = 0
    for i in range(len(memo)):
        for j in range(i + 1, len(memo)):
            if isEqual(grid, memo[i], memo[j]):
                cnt += 1

    return cnt

grid = [
[0,1,1,0,0],
[0,0,1,0,0],
[0,0,0,1,1],
[0,0,0,0,1]]
# output: 1 pair of equal matrix
res = equalMatrix(grid)
print(res)

#1 1 0 0 
#1 1 1 0
#0 0 0 0
#0 1 1 0
#0 1 1 0
#output 0 pair of equal matrix






