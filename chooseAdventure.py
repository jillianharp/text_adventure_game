# Jillian Harper
# COS 121
# 12/8
# Final Project - Choose Your Own Adventure

def ShowLibrary(world):
    print("Welcome to your journey!")
    print("You are on an unknown island.")
    print("You have obtained a map.")
    print("There are three routes you can take.")

    print("What route will you take?")

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
        world
        return
    if userInput == "three":
        print("You have chosen the underground path.")
        print("Head east until you reach the cave.")
        print("It shouldn't be too far.")
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
    if "conch shell" not in world["inv"]:
        print("You find a conch shell in the sand.")
        print("Take the conch shell,")
        print("you might need to use it to make noise.")
        world["inv"].append("conch shell")
    else:
        print("Nothing but the conch shell here.")
        print("Continue west.")

def showUnderground(world):
    print("Keep heading east,")
    print("you will reach the cave soon.")
    if "shield" not in world["inv"]:
        print("You step on something hiding under some dirt.")
        print("It appears to be a shield.")
        print("This could come in handy.")
        world["inv"].append("shield")
    else:
        print("Only the shield here.")
        print("Continue east.")
