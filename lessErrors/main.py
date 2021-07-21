from typing import final
from game.eightNumberBoard import EightNumberBoard
from heapq import heappush, heappop
import time
import itertools
import copy
import time

def printNode(node):
    print(node[0][0],node[0][1],node[0][2])
    print(node[1][0],node[1][1],node[1][2])
    print(node[2][0],node[2][1],node[2][2])
    global nodeNumber
    print('Node:', nodeNumber)
    print('------')
    nodeNumber += 1

def toZero(a):
    return 0 if a == None else a

def checkFinal(node, finalNode):
    if node == finalNode:
        printNode(node)
        return True
    if node not in visitedList:
        printNode(node)
        nodeList.append(node)
        visitedList.append(node)
    return False

def heuristic(node, finalNode):
    errors = 0

    for i in range(len(node)):
        for j in range(len(node)):
            if node[i][j] != finalNode[i][j]:
                errors += 1

    return errors

if __name__ == '__main__':
    board = EightNumberBoard()
    
    startNode = board.getBoard()
    print(startNode)
    finalNode = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    
    found = False
    nodeNumber = 0
    visitedList = []
    nodeList = []
    nodeList.append(startNode)
    visitedList.append(startNode)

    t0 = time.time()

    found = False

    while not found:
        fList = []
        for node in nodeList:
            h = heuristic(node, finalNode)
            heappush(fList, (h, node))

        currentNode = nodeList.pop(
            nodeList.index(
                heappop(fList)[1]
            )
        )

        blankIndex = [[i, n.index(0)] for i, n in enumerate(currentNode) if 0 in n][0]

        if board.canMoveTop(blankIndex):
            topNode = board.top(currentNode, blankIndex[0], blankIndex[1])
            found = checkFinal(topNode, finalNode)

        if board.canMoveLeft(blankIndex) and found == False:
            leftNode = board.left(currentNode, blankIndex[0], blankIndex[1])
            found = checkFinal(leftNode, finalNode)

        if board.canMoveRight(blankIndex) and found == False:
            rightNode = board.right(currentNode, blankIndex[0], blankIndex[1])
            found = checkFinal(rightNode, finalNode)

        if board.canMoveBottom(blankIndex) and found == False:
            bottomNode = board.bottom(currentNode, blankIndex[0], blankIndex[1])
            found = checkFinal(bottomNode, finalNode)

    t1 = time.time()
    print('Time:', t1-t0)
    print('------')