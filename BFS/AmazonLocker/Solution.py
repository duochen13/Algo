
"""
input:
[[0,1,0,0,1],
 [0,0,0,0,0],
 [0,1,0,1,0],
 [0,0,0,0,0]]
"""

def shortestDistance(grid):
    if not grid or not grid[0]:
        return -1
    m, n = len(grid), len(grid[0])

    dirs = [[-1,0],[1,0],[0,-1],[0,1]]
    distance = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                visited = [[False for _ in range(n)] for _ in range(m)]
                level = 1
                q = [[i,j]]
                while q:
                    N = len(q)
                    for _ in range(N):
                        x, y = q.pop(0)
                        for a, b in dirs:
                            nx, ny = x + a, y + b
                            # within range && not visited
                            if nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                                # marked as visited
                                visited[nx][ny] = True
                                # construct distance field
                                distance[nx][ny] += level
                                # add neighbors to the queue
                                q.append([nx, ny])
                    level += 1
    
    print("distance:{}".format(distance))

grid = [
 [0,1,0,0,1],
 [0,0,0,0,0],
 [0,1,0,1,0],
 [0,0,0,0,0]]
"""
distance:
[[15, 0, 9, 9, 0],
[13, 9, 9, 9, 11],
[15, 0, 9, 0, 13],
[17, 15, 13, 13, 15]]
"""
shortestDistance(grid)


