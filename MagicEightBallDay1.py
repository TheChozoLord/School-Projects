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
      " 2: get your fortune told"
      " 3: pick specific fortune"
      " 4: leave")

menuInput = (input("enter number of option you wish to persue"))

if menuInput == "2":
    fortuneRandomizer = random.randint(0, 9)
    print (fortune[fortuneRandomizer])
if menuInput == "1":
    print(fortune) 
if menuInput == "3":
    specific = input("Please input the number of the fortune you want:")
    print (fortune[specific])
else:
    print ("Probably for the best.")