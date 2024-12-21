
from boardTools import *
from inputs import *




def main():

    f = open("story.txt", "r")
    dataString = f.read()
    print(dataString)

    world = {}
    loc = {
        "x": 2,
        "y": 2
    }

    world["board"] = createBoard(5)
    world["playerLoc"] = loc
    world["playerName"] = getUserName()


    input("Press enter to start your adventure.")



    while True:
        printBoard(world)
        print("What path would you like to take? Choose a route:")
        print("1: Jungle")
        print("2: Beach")
        print("3: Cave")

        userInput = input("Enter your choice (1, 2, or 3): ").strip()

        if userInput == '1':
            from routeOneBattle import jungleBattle
            loc["x"] = 2
            loc["y"] = 1
            print("You are now in the Jungle.")
            jungleBattle(world["playerLoc"])
        elif userInput == '2':
            from routeTwoBattle import beachBattle
            loc["x"] = 1
            loc["y"] = 2
            print("You are now at the Beach.")
            beachBattle(world["playerLoc"])
        elif userInput == '3':
            from routeThreeBattle import caveBattle
            loc["x"] = 3
            loc["y"] = 2
            print("You are now in the Cave.")
            caveBattle(world["playerLoc"])

        else:
            print("Invalid input. Please choose a valid path (1, 2, or 3).")

    
        

        
    
    


main()
