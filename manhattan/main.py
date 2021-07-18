from game.eightNumberBoard import EightNumberBoard
from heapq import heappush, heappop
import time
import itertools

def toZero(a):
    return 0 if a == None else a

def manhattan(a):
    result = 0

    node = list(itertools.chain(*a))

    for current, target in enumerate(node):
        currentRow = int(current/3)
        currentColumn = current%3
        targetRow = int(target/3)
        targetColumn = target%3
        result += abs(currentRow-targetRow) + abs(currentColumn-targetColumn)

    return result

if __name__ == '__main__':
    board = EightNumberBoard()
    
    finalNode = [[0,1,2], [3,4,5], [6,7,8]]
    
    priorityQueue = []
    
    heappush(priorityQueue, (0, board.getBoard()))

    checkFinal = lambda x: x == finalNode

    t0 = time.time()

    found = False

    while (not found and len(priorityQueue) != 0):
        print(priorityQueue)
        currentNode = heappop(priorityQueue)[1]
        print(priorityQueue)

        blankIndex = [[i, n.index(0)] for i, n in enumerate(currentNode) if 0 in n][0]
        
        if currentNode == finalNode:
            print("Daleee")
            break

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

        print("Queue {}".format(len(priorityQueue)))

        #break

    t1 = time.time()
    print('Time:', t1-t0)
    print('------')