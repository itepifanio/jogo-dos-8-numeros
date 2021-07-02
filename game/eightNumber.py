from .board import Board
from random import choice

class EightNumber:
    def __init__(self):
        self.size = 3
        self.board = Board(self.size)
        queue = list(range(0,9))
        
        for i in range(self.size):
            for j in range(self.size):
                value = choice(queue)
                queue.remove(value)
                
                self.board.update(i,j, value if value != 0 else None)

    def left(self, i, j):
        pass

    def right(self, i, j):
        pass

    def bottom(self, i, j):
        pass

    def top(self, i, j):
        pass
    
    def __str__(self):
        return self.board.__str__()