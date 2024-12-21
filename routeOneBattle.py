from random import *
from inputs import *

def diceRoll(roll):
    rSplit = roll.split("d")
    numDice = int(rSplit[0])
    diceSize = int(rSplit[1])

    diceList = []
    for i in range(numDice):
        diceList.append(randint(1, diceSize))
    return diceList

def turn(attacker, defender, who):
    if who == "player":
        print("Choose your fate: ")
        print("1: Fight")
        print("2: Don't fight")
        decision = input()
    else:
        if (randint(1,2) == 1):
            decision = "1"
        else:
            decision = "2"

    if decision == "1":
        defender["hp"] -= attacker["atk"]
        print(f"{attacker['name']} hits {defender['name']} for {attacker['atk']} damage")

    elif decision == "2":
        healAmt = sum(diceRoll("1d4"))
        attacker["hp"] += healAmt
        print(f"{attacker['name']} gains {healAmt} hp")

def turn2(attacker, defender, who):
    if who == "player":
        print("Choose your fate: ")
        print("1: Don't fight")
        print("2: Continue fighting")
        decision = input()
    else:
        if (randint(1,2) == 1):
            decision = "1"
        else:
            decision = "2"

    if decision == "1":
        healAmt = sum(diceRoll("1d4"))
        attacker["hp"] += healAmt
        print(f"{attacker['name']} regains {healAmt} hp")

    elif decision == "2":
        attacker["hp"] -= defender["atk"]
        print(f"{defender['name']} hits {attacker['name']} for {defender['atk']} damage")

def turn3(attacker, defender, who):
    decision = None
    if who == "player":
        print(f"{attacker['name']} runs towards you")
        print("What do you choose?: ")
        print("1: Dodge the attack")
        print("2: Attempt to block")
    else:
        if (randint(1,2) == 1):
            decision = "1"
        else:
            decision = "2"

    if decision == "1":
        healAmt = sum(diceRoll("1d4"))
        attacker["hp"] -= defender["atk"]
        print("You dodge the attack causing the enemy to fly past you")
        print(f"{attacker['name']} hits a tree, causing {defender['atk']} damage")

    elif decision == "2":
        defender["hp"] -= attacker["atk"]
        print(f"{attacker['name']} hits {defender['name']} for {attacker['atk']} damage")



def jungleBattle(player, enemy):
    print(f"{enemy['name']} nears {player['name']}, looking for a battle")
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

    playerName = getUserName()
    player = {
        "name": playerName,
        "hp": 20,
        "atk": 5
    }
        
    enemy = {
        "name": "Tree Hugger",
        "hp": 30,
        "atk": 10
    }

    result = jungleBattle(player, enemy)
    if result == "enemy dead":
        print(f"The {enemy['name']} crashes to the ground and withers away")
        print("You have survived your great battle.")
        print("Your reward is ten million dollars!")
        print("Congratulations! Enjoy your prize.")
    else:
        print(f"{player['name']} has reached their fatal fate.")
        print(f"This is the end of the journey for {playerName}...")
    return


main()