from game.eightNumberBoard import EightNumberBoard
from queue import Queue 
import copy
import time

def printNode(node):
    print(node[0][0],node[0][1],node[0][2])
    print(node[1][0],node[1][1],node[1][2])
    print(node[2][0],node[2][1],node[2][2])
    global nodeNumber
    print('Node:', nodeNumber)
    print('Depth:', len(node[9:]))
    #print('Moves:', node[9:])
    print('------')
    nodeNumber += 1

def checkFinal(node):
    if node == finalNode:
        printNode(node)
        return True
    if node not in visitedList:
        printNode(node)
        queue.put(node)
        visitedList.append(node)
    return False

if __name__ == '__main__':
    board = EightNumberBoard()
    finalNode = [[1,2,3], [8,None,4], [7,6,5]]
    
    found = False
    nodeNumber = 0
    visitedList = []
    queue = Queue()
    queue.put(board.getBoard())
    visitedList.append(board.getBoard())
    printNode(board.getBoard())
    t0 = time.time()

    while (not found and not queue.empty()):
        currentNode = queue.get()
        blankIndex = [[i, n.index(None)] for i, n in enumerate(currentNode) if None in n][0]
        
        if board.canMoveTop(blankIndex):
            found = checkFinal(
                board.top(currentNode, blankIndex[0], blankIndex[1])
            )
        if board.canMoveLeft(blankIndex) and found == False:
            found = checkFinal(
                board.left(currentNode, blankIndex[0], blankIndex[1])
            )
        if board.canMoveRight(blankIndex) and found == False:
            found = checkFinal(
                board.right(currentNode, blankIndex[0], blankIndex[1])
            )
        if board.canMoveBottom(blankIndex) and found == False:
            found = checkFinal(
                board.bottom(currentNode, blankIndex[0], blankIndex[1])
            )

    t1 = time.time()
    print('Time:', t1-t0)
    print('------')
    