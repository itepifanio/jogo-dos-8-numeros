import copy
from .board import Board
from random import choice

class EightNumberBoard:
    def __init__(self):
        self.size = 3
        self.board = Board(self.size)
        queue = list(range(0,9))
        
        for i in range(self.size):
            for j in range(self.size):
                value = choice(queue)
                queue.remove(value)
                
                self.board.update(i,j, value if value != 0 else None)

    def getBoard(self):
        return self.board

    def canMoveLeft(self, i, j):
        try:
            return self.board.matrix[i][j-1] == None
        except:
            return False

    def left(self, i, j):
        if self.canMoveLeft(i, j):
            self.board.matrix[i][j-1] = self.board.matrix[i][j]
            self.board.matrix[i][j] = None
        else:
            raise Exception("Cant go left")

    def canMoveRight(self, i, j):
        try:
            return self.board.matrix[i][j+1] == None
        except:
            return False

    def right(self, i, j):
        if self.canMoveRight(i, j):
            self.board.matrix[i][j+1] = self.board.matrix[i][j]
            self.board.matrix[i][j] = None
        else:
            raise Exception("Cant go right")

    def canMoveBottom(self, i, j):
        try:
            return self.board.matrix[i+1][j] == None
        except:
            return False

    def bottom(self, i, j):
        if self.canMoveBottom(i, j):
            self.board.matrix[i+1][j] = self.board.matrix[i][j]
            self.board.matrix[i][j] = None
        else:
            raise Exception("Cant go bottom")

    def canMoveTop(self, i, j):
        return i != 0 and j not in [0,1,2]

    def top(self, node, i, j):
        upNode = copy.deepcopy(node)
        upNode[i][j] = upNode[i][j]
        upNode[i][j] = None
        
        return upNode
    
    def __str__(self):
        return self.board.__str__()