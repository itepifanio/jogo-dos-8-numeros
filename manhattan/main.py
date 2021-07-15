from game.eightNumberBoard import EightNumberBoard
from heapq import heappush, heappop
import time

def toZero(a):
    return 0 if a == None else a

def manhattan(node):
    distance = 0
    for row in node:
        for current, target in enumerate(row):
            currentRow = int(current/3)
            currentColumn = current%3
            targetRow = int(target/3)
            targetColumn = target%3
            distance += abs(currentRow-targetRow) + abs(currentColumn-targetColumn)
    return distance
    result = 0

    for i in range(len(a)):
        result += sum(abs(val1-val2) for val1, val2 in zip(a[i],b[i]))

    return result

if __name__ == '__main__':
    board = EightNumberBoard()
    
    finalNode = [[1,2,3], [8,0,4], [7,6,5]]
    
    priorityQueue = []
    
    heappush(priorityQueue, (0, board.getBoard()))

    checkFinal = lambda x: x == finalNode

    t0 = time.time()

    found = False

    while (not found and len(priorityQueue) != 0):
        print(priorityQueue)
        currentNode = heappop(priorityQueue)[1]

        blankIndex = [[i, n.index(0)] for i, n in enumerate(currentNode) if 0 in n][0]
        
        index = 0

        if board.canMoveTop(blankIndex):
            topNode = board.top(currentNode, blankIndex[0], blankIndex[1])
            found = checkFinal(topNode)
            heappush(
                priorityQueue, (manhattan(topNode), topNode)
            )

        if board.canMoveLeft(blankIndex) and found == False:
            leftNode = board.left(currentNode, blankIndex[0], blankIndex[1])
            found = checkFinal(leftNode)
            heappush(
                priorityQueue, (manhattan(leftNode), leftNode)
            )

        if board.canMoveRight(blankIndex) and found == False:
            rightNode = board.right(currentNode, blankIndex[0], blankIndex[1])
            found = checkFinal(rightNode)
            heappush(
                priorityQueue, (manhattan(rightNode), rightNode)
            )

        if board.canMoveBottom(blankIndex) and found == False:
            bottomNode = board.bottom(currentNode, blankIndex[0], blankIndex[1])
            found = checkFinal(bottomNode)
            heappush(
                priorityQueue, (manhattan(bottomNode), bottomNode)
            )

    t1 = time.time()
    print('Time:', t1-t0)
    print('------')