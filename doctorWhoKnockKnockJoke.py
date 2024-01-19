# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:33:36 2024

@author: owen.merrill
"""

name = input("Hello. What's your name? ")
question = f"""Nice to meet you {name}. Would you like to hear a joke? (Y/N)"""
print (question)
answer = input(" ")
if answer == "Y" :
    print ("Great! Knock knock!")
    who = input(" ")
    if who == "Whos there?" :
        print ("Doctor")
        dr = input(" ")
        if dr == "Doctor who?" :
            "Play .mp3 file."
        else:
            print("You're supposed to say Doctor Who?")
    else:
        print("You're supposed to say Who's there?")
else:
    print("Oh. Ok.")