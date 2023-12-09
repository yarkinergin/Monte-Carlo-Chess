import copy

class Node:
    def __init__(self, chessBoard: list, whosMove, move):
        self.children = []
        self.parent = None
        self.checkmated = False
        self.whosMove = whosMove
        self.moveFrom = move
        self.chessBoard = copy.deepcopy(chessBoard)
        self.data = 0
        self.sims = 0
   
    def PrintTree(self):
        print(self.data)    