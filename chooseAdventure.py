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
        world["loc"] = "jungle"
        return
    if userInput == "two":
        print("You have chosen the path across the beach.")
        print("Watch out for the birds!")
        world
        return
    if userInput == "three":
        print("You have chosen the underground path.")
        print("Head east until you reach the cave.")
        print("It shouldn't be too far.")
        return

