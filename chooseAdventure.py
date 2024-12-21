# Jillian Harper
# COS 121
# 12/8
# Final Project - Choose Your Own Adventure

def ShowLibrary(world):

    userInput = input()
    if userInput == "one":
        print("You have chosen the path through the jungle.")
        print("Rough terrain ahead!")
        print("Use caution!")
        print("Head north.")
        world["loc"] = "jungle"
        return
    if userInput == "two":
        print("You have chosen the path across the beach.")
        print("Watch out for the birds!")
        print("Head west to reach the beach.)")
        world["loc"] = "beach"
        return
    if userInput == "three":
        print("You have chosen the path to the cave.")
        print("Head east until you reach the cave.")
        print("It shouldn't be too far.")
        world["loc"] = "cave"
        return

def showJungle(world):
    print("You've reached the edge of the jungle.")
    print("Prepare to begin your journey through the jungle.")
    if "walking stick" not in world["inv"]:
        print("You find a walking stick on the ground.")
        print("Take the walking stick,")
        print("you're going to need it.")
        world["inv"].append("walking stick")
    else:
        print("Nothing but the walking stick here.")
        print("Continue north.")

def showBeach(world):
    print("You will see sand ahead soon.")
    print("Prepare to begin your journey across the beach.")
    if "shield" not in world["inv"]:
        print("You find a shield in the sand.")
        print("Take the shield,")
        print("it could come in handy.")
        world["inv"].append("shield")
    else:
        print("Nothing but the shield here.")
        print("Continue west.")

def showUnderground(world):
    print("Keep heading east,")
    print("you will reach the cave soon.")
    if "baseball bat" not in world["inv"]:
        print("You step on something hiding under some dirt.")
        print("It appears to be a baseball bat.")
        print("This could be useful.")
        world["inv"].append("baseball bat")
    else:
        print("Only the baseball bat here.")
        print("Continue east.")

