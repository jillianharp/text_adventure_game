def getUserDir():

    validCommands = ['one','two','three']
    while True:
        userInput = input("Choose a route (one,two,three): ")
        userInput = userInput.lower().strip()
        if userInput not in validCommands:
            print("Invalid choice. Choose from (one,two,three): ")
            continue
        return userInput
    
def getUserName():
    while True:
        userInput = input("Enter your character's name\n:")
        userInput = userInput.upper().strip()
        if len(userInput) > 15:
            print("15 characters or less please")
            continue
        if len(userInput) < 3:
            print("Name must be longer than three characters")
            continue

        return userInput