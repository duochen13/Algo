
# initialize a chess board with width and height, and # 'x's,
# requirements: randomly allocated
# x
# o

# error handling, edge cases
# pros and cons when
import random

class Board:
    def __init__(self, width, height, num_mine):
        self.width = width
        self.height = height
        self.num_mine = num_mine
        self.board = [['o' for _ in range(width)] for _ in range(height)] 

    def initialize(self):
        positions = [(r, c) for r in range(self.height) for c in range(self.width)]
        random.shuffle(positions)
        for i in range(self.num_mine):
            x, y = positions[i]
            self.board[x][y] = 'x'

    def click_board(self, x, y):
        # out of range err
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            raise Exception('You click out of range')
        # bomb!
        if self.board[x][y] == 'x':
            raise Exception('End!')
        self.board[x][y] = '*'
        # display surrounding mines
        mines = 0
        for a, b in [[-1,0],[1,0],[0,-1],[0,1]]:
            if x + a < 0 or x + a >= self.height or y + b < 0 or y + b >= self.width:
                continue
            if self.board[x + a][y + b] == 'x':
                mines += 1
        for a, b in [[-1,0],[1,0],[0,-1],[0,1]]:
            self.board[x + a][y + b] = str(mines)

    def print_board(self):
        tmp = ''
        for i in range(self.height):
            for j in range(self.width):
                tmp += self.board[i][j] + ' '
            tmp += '\n'
        print(tmp)

    

# pros and con
board = Board(width=5, height=5, num_mine=4)
board.initialize()
board.print_board()
board.click_board(1,1)
board.print_board()


