from game.eightNumberBoard import EightNumberBoard

def main():
    eightNumber = EightNumberBoard()
    print(eightNumber)
    
    board = eightNumber.getBoard().matrix
    for i in range(len(board)):
        for j in range(len(board)):
            if(eightNumber.canMoveBottom(i, j)):
                eightNumber.bottom(i, j)
                print(eightNumber)



if __name__ == "__main__":
    main()