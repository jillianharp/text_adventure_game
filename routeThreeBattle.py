from random import *

def diceRoll(roll):
    rSplit = roll.split("d")
    numDice = int(rSplit[0])
    diceSize = int(rSplit[1])

    diceList = []
    for i in range (numDice):
        diceList.append(randint(1, diceSize))
    return diceSize

def turn(attacker, defender, who):
    if who == "player":
        print("Choose your fate: ")
        print("1: Fight")
        print("2: Don't fight")
        decision = input()
    else:
        if (randint(1,2) == 1):
            decision == "1"
        else:
            decision == "2"

    if decision == "1":
        defender["hp"] -= attacker["atk"]
        print(f"{attacker["name"]} hits {defender["name"]} for {attacker["atk"]} damage")

    if decision == "2":
        healAmt = sum(diceRoll("1d4"))
        attacker["hp"] += healAmt
        print(f"{attacker["name"]} gains {healAmt} hp")

def turn2(attacker, defender, who):
    if who == "player":
        print("Choose your fate: ")
        print("1: Don't fight")
        print("2: Continue fighting")
        decision = input()
    else:
        if (randint(1,2) ==1):
            decision == "1"
        else:
            decision == "2"

    if decision == "1":
        defender["hp"] -= attacker["atk"]
        print(f"{attacker["name"]} hits {defender["name"]} for {attacker["atk"]} damage")
    
    if decision == "2":
        attacker["hp"] -= defender["atk"]
        print(f"{defender["name"]} hits {attacker["name"]} for {defender["atk"]}")

def turn3(attacker, defender, who):
    if who == "player":
        print(f"{attacker["name"]} lunges towards you")
        print("What do you choose to do?: ")
        print("1: Use your baseball bat")
        print("2: Run away")
        decision = input()
    else:
        if (randint(1,2) ==1):
            decision == "1"
        else:
            decision == "2"

    if decision == "1":
        healAmt = sum(diceRoll("1d4"))
        defender["hp"] += healAmt
        print(f"You hit {attacker["name"]} and regained {healAmt} hp")
        print(f"{defender["name"]} regain {healAmt} hp")

    if decision == "2":
      defender["hp"] -= attacker["atk"]
      print(f"{attacker["name"]} attacks {defender["name"]} for {attacker["atk"]} damage")


def beachBattle(player, enemy):
    print(f"{enemy["name"]} crawls out from the cave")
    while True:
        turn(player, enemy, "player")
        turn(enemy, player, "enemy")
        print(f"{player['name']} has {player['hp']} hp left")
        print(f"{enemy['name']} has {enemy['hp']} hp left")
        if (player["hp"] <= 0):
            return "player dead"
        if (enemy["hp"] <= 0):
            return "enemy dead"
        
        turn2(player, enemy, "player")
        turn2(enemy, player, "enemy")
        print(f"{player['name']} has {player['hp']} hp left")
        print(f"{enemy['name']} has {enemy['hp']} hp left")
        if (player["hp"] <= 0):
            return "player dead"
        if (enemy["hp"] <= 0):
            return "enemy dead"
        
        turn3(player, enemy, "player")
        turn3(enemy, player, "enemy")
        print(f"{player['name']} has {player['hp']} hp left")
        print(f"{enemy['name']} has {enemy['hp']} hp left")
        if (player["hp"] <= 0):
            return "player dead"
        if (enemy["hp"] <= 0):
            return "enemy dead"
        
def main():
    player = {
        "name": {player["name"]},
        "hp": 20,
        "atk": 5
    }

    enemy = {
        "name": "Spooky Skeleton",
        "hp": 30,
        "atk": 15
    }

    result = beachBattle(player, enemy)
    if result == "enemy dead":
        print(f"The {enemy["name"]} breaks apart in front of you")
        print("You have survived your great battle.")
        print("Your reward is a brand new car!")
        print("But you'll have to find it.")
        print("Congratulations! Enjoy your new ride...once you've found it.")
    else:
        print(f"{player["name"]} has reached their final fate.")
        print(f"This is the end of the journey for {player["name"]}")
    pass

main()