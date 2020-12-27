
"""
1: building, 2: obstacle, 0: empty cell
Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

output: 7 (point[1,2]) = 3 + 3 + 1
"""

def shortestDistance(grid):
    if not grid or not grid[0]:
        return -1
    m, n = len(grid), len(grid[0])
    distance = [[0 for _ in range(n)] for _ in range(m)]
    reach = [[0 for _ in range(n)] for _ in range(m)]   
    dirs = [[-1,0],[1,0],[0,-1],[0,1]]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                level = 1
                visited = [[False for _ in range(n)] for _ in range(m)]
                q = [[i, j]]
                while q:
                    N = len(q)
                    # bfs on current level
                    for _ in range(N):
                        x, y = q.pop(0)
                        for a, b in dirs:    
                            nx, ny = x + a, y + b
                            if nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                                visited[nx][ny] = True
                                distance[nx][ny] += level
                                reach[nx][ny] += 1
                                q.append([nx, ny])
                    level += 1
    print("distance:{}".format(distance))
    res = float('inf') # +inf
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                res = min(res, distance[i][j])

    return res

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
res = shortestDistance(grid)

print(res)
