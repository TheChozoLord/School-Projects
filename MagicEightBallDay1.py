# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

fortune = [
"Nah", "its no use", "Good luck with that", 
"probably not", "Im not gonna stop you", 
"go for it", "heck yeah", 
"maybe", "yes yes yes", 
"live and learn"]

print("Hello! What do you want to do?"
      " 1: show all fortunes"
      " 2: pick specific fortune"
      " 3: get your fortune told"
      " 4: leave")

menuInput = (input("enter number of option you wish to persue: "))

if menuInput == "3":
    fortuneRandomizer = random.randint(0, 9)
    input("What is your question? ")
    print (fortune[fortuneRandomizer])
if menuInput == "1":
    for i, fortune in enumerate(fortune):
        print(f"{i} (fortune[i])") 
if menuInput == "2":
    specific = input("Please input the number of the fortune you want:")
    specificInt = int(specific)
    print (fortune[specificInt])
if menuInput =="4":
    print ("Probably for the best.")
else:
    print("Please enter a valid input next time")