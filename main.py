from boardTools import *
from inputs import *
from routeOneBattle import *



def main():
    world = {}
    loc = {
        "x": 2,
        "y": 2
    }

    world["board"] = createBoard(5)
    world["playerLoc"] = loc
    world["playerName"] = getUserName()

    while True:
        printBoard(world)
        userInput = getUserDir()
        if userInput == 'one' and loc["y"] > 0:
            loc["y"] -= 1
        if userInput == 'two' and loc["x"] > 0:
            loc["x"] -= 1
        if userInput == 'three' and loc["x"] < len(world["board"])-1:
            loc["x"] += 1


main()
