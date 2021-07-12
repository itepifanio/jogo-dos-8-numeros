from queue import Queue 
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
    startNode = [[1,5,4], [3,7,2], [6,8,None]]
    finalNode = [[None,1,2], [3,4,5], [6,7,8]]
    
    found = False
    nodeNumber = 0
    visitedList = []
    queue = Queue()
    queue.put(startNode)
    visitedList.append(startNode)
    printNode(startNode)
    t0 = time.time()

    #time.sleep(2)

    while (not found and not queue.empty()):
        currentNode = queue.get()
        blankIndex = [[i, n.index(None)] for i, n in enumerate(currentNode) if None in n][0]
        
        if blankIndex != [0, 0] and blankIndex != [0,1] and blankIndex != [0,2]:
            upNode = copy.deepcopy(currentNode)
            print(upNode)
            upNode[blankIndex[0]][blankIndex[1]] = upNode[blankIndex[0]-1][blankIndex[1]]
            upNode[blankIndex[0]-1][blankIndex[1]] = None
            found = checkFinal(upNode)
        if blankIndex != [0,3] and blankIndex != [1,0] and blankIndex != [2,0] and found==False:
            leftNode = copy.deepcopy(currentNode)
            leftNode[blankIndex[0]][blankIndex[1]] = leftNode[blankIndex[0]][blankIndex[1]-1]
            leftNode[blankIndex[0]][blankIndex[1]-1] = None
            found = checkFinal(leftNode)
        if blankIndex!=[2,0] and blankIndex!=[2,1] and blankIndex!= [2,2] and found==False:
            downNode = copy.deepcopy(currentNode)
            downNode[blankIndex[0]][blankIndex[1]] = downNode[blankIndex[0]+1][blankIndex[1]]
            downNode[blankIndex[0]+1][blankIndex[1]] = None
            found = checkFinal(downNode)
        if blankIndex!=[0,2] and blankIndex!= [1,2] and blankIndex!=[2,2] and found==False:
            rightNode = copy.deepcopy(currentNode)
            rightNode[blankIndex[0]][blankIndex[1]] = rightNode[blankIndex[0]][blankIndex[1]+1]
            rightNode[blankIndex[0]][blankIndex[1]+1] = None
            found = checkFinal(rightNode)

    t1 = time.time()
    print('Time:', t1-t0)
    print('------')
    