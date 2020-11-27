
class Chess:

    def __init__(self):
        self.board = [['. ' for _ in range(8)] for _ in range(8)]
        col = 0
        for node in ['r','n','b','q','k','b','n','r']:
            self.board[0][col] = node + ' '
            self.board[7][col] = chr(ord(node) - 32) + ' '
            col += 1
        for j in range(8):
            self.board[1][j] = 'p '
            self.board[6][j] = 'P '

    def printBoard(self):
        for i in range(8):
            print('{} '.format(8 - i), end='')
            for j in range(8):
                print(self.board[i][j] + ' ', end='')
            print('')
        print('  a  b  c  d  e  f  g  h\n')

    def move(self, start, end):
        y1, x1, y2, x2 = start[0], start[1], end[0], end[1]
        # ERROR: Out of range
        y1 = ord(y1) - ord('a')
        x1 = int(x1) - 1
        node = self.board[x1][y1]
        self.board[x1][y1] = '. '
        y2 = ord(y2) - ord('a')
        x2 = int(x2) - 1
        self.board[x2][y2] = node

chess = Chess()
chess.printBoard()
chess.move('d2', 'd4')
chess.printBoard()
