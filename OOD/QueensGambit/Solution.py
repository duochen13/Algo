import sys

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

    # ex: move("d2","d4")
    def move(self, start, end):
        y1, x1, y2, x2 = start[0], start[1], end[0], end[1]
        # ERROR: Out of range
        y1 = ord(y1) - ord('a')
        x1 = 8 - int(x1)
        startNode = self.board[x1][y1]
        isBalck = startNode.islower()
        self.board[x1][y1] = '. '
        y2 = ord(y2) - ord('a')
        x2 = 8 - int(x2)
        endNode = self.board[x2][y2]
        self.board[x2][y2] = startNode
        # Take the opponent's node
    
    
chess = Chess()
chess.printBoard()

whiteTurn = True
start = end = ""

QueensGambit = [
"d2 d4",
"d7 d5",
"c2 e4",
"d5 c4",
"e2 e3",
"b7 b5",
"a2 a4",
"c7 c6",
"a4 b5",
"c6 b5",
"d1 f3"
]


for line in QueensGambit:
    # line: move("d2", "d4")
    line = line.rstrip()
    start, end = line.split(" ")
    chess.move(start, end)
    print("[{}] move from {} to {}".format("White" if whiteTurn else "Black", start, end))
    chess.printBoard()
    whiteTurn = not whiteTurn

    
