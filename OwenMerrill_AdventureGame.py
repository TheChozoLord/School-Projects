# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 10:10:04 2024

@author: owen.merrill
"""
def getGame():
    game = {
        "start": ["You are in a plane that is on fire and falling out of the sky.", "Stay on plane", "stay", "Jump into Ocean", "jump"], 
        "stay": ["You stay strapped in you seatbelt as the plane falls out of the sky. Eventualy it hits the ground and skidds to a stop.", "Stay near plane", "wait", "Search for suplies", "search"], 
        "jump": ["You grab a life vest and jump out the side of the plane. You hit the water and die instantly.", "Restart", "start", "Quit", "quit"], 
        "wait": ["You stay near the plane.", "Rummage through luggage", "rummage", "Make sure the plane wont explode", "maintenence"], 
        "search": ["You wander off in search of suplies, but get lost and die.", "Restart", "start", "Quit", "quit"], 
        "rummage": ["You rummage through your dead fellow passengers luggage and find a lighter, several snacks, plenty of cloth, a bowie knife, and the american nuclear codes.", "Light a fire", "fire", "examine nuclear codes.", "codes"], 
        "maintinence": ["You find a bit of fuel leaking out of the plane, but you dont have anything to plug it with. ", "Light a fire", "fire", "Rummage through luggage", "Rummage"], 
        "fire": ["You get a good fire going but a few sparks from the fire float away and hit some feul leaking from the plane causing it to explode in a massive fireball.", "Restart", "start", "Quit", "quit"], 
        "codes": ["As you look over the codes, you spot a helicopter approaching. You recognize it as the one that shot down your plane.", "Run into jungle", "run", "Prepare to fight.", "fight"], 
        "run": ["You take the nuclear codes, snacks, lighter, and bowie knife and charge into the jungle. You soon hear people behind you, and you push through some vines to find yourself in a small shrine with a glowing orb set on a pedastal in the middle.", "touch it", "touch", "Hide", "hide"], 
        "fight": ["As you prepare to fight, you are hit with a misile and die.", "Restart", "start", "Quit", "quit"], 
        "Touch it": ["As you touch the orb you are filled with the power of the sun. The people who were chasing you burst into the shrine behind you guns raised, and are instantly vaporised by your majesty. You look to the sky and fly away, as the island below you crumbles.", "Restart", "start", "End", "quit"], 
        "hide": ["You duck behind the altar and hide. Three men burst into the shrine shortly afterwards guns raised, searching for you. One of them reaches out to touch the orb, and when they do it explodes in a burst of energy vaporising everyone in the room.", "Restart", "start", "Quit", "quit"], 
        "quit": ["Game Over", "", "", "", ""], 
    }
    return(game)

def main():
    game = getGame()
    keepGoing = True
    activeNode = "start"
    while(keepGoing == True):
    
        if activeNode == "quit":
            keepGoing = False
        else:
            activeNode = playNode(activeNode, game)
            
def playNode(activeNode, game):
    (description, menu1, node1, menu2, node2) = game[activeNode]

    print(f"""
          {description}
          1. {menu1}
          2. {menu2}
          """)
    choice = input("please type the number that corresponds to your desired course of action: ")
    if choice == "1":
        activeNode = node1
    elif choice == "2":
        activeNode = node2
    else:
        print("Improper input. Please try again.")
    return(activeNode)

main()