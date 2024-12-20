def createBoard(boardSize):
    board = []
    for row in range(boardSize):
        board.append([])
        for col in range(boardSize):
            board[row].append(0)
            
    return board



def printBoard(world):
    outputString = ""

    board = world["board"]
    for row in range(len(board)):
        for col in range(len(board)):

            if world["playerLoc"]["x"] == col and \
                world["playerLoc"]["y"] == row:
                outputString += f"[{'X':>2}]"
            elif board[row][col] == 0:
                outputString += f"[{"":2}]"

        outputString += "\n"
    print(outputString, end="")
