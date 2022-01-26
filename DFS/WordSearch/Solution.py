"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


# idea
"""
for each entry in m * n matrix
   curWord="",
           /   \
         "A"     "B"
         /  \      / \
       "AS"  "AB"    

avoid inf loop: marked as visiting {
    visited: 2, visiting: 1, unvisited: 0
}

terminal state: length > len(word), out of bound
"""

def dfs(board, visited, i, j, index, word):
    m, n = len(board), len(board[0])
    directions = [[-1,0],[1,0],[0,1],[0,-1]]
    # length out of bound or visited
    if index >= len(word) or word[index] != board[i][j] or visited[i][j] == 2:
        return False
    # find the matched word 
    if index == len(word) - 1 and board[i][j] == word[index]:
        return True
    # mark current location as visiting
    visited[i][j] = 1
    # dfs 
    for a, b in directions:
        x, y = i + a, j + b 
        if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] != 0:
            continue 
        if dfs(board, visited, x, y, index + 1, word):
            return True 
    # mark current location as visited 
    visited[i][j] = 2
    return False



def exist(board, word):
    m, n = len(board), len(board[0])
    visited = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if dfs(board, visited, i, j, 0, word):
                return True
    return False
    



# test
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
assert exist(board, word) == True
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
assert exist(board, word) == True
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
assert exist(board, word) == False

