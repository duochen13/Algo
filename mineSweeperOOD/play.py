
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
        tmp = 0
        while tmp < self.num_mine:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] == 'o':
                tmp += 1
                self.board[y][x] = 'x'
        print(self.board)

    def print_board(self):
        tmp = ''
        for i in range(self.height):
            for j in range(self.width):
                tmp += self.board[i][j] + ' '
            tmp += '\n'
        print(tmp)

# pros and con
board = Board(width=3, height=3, num_mine=4)
board.initialize()
board.print_board()



