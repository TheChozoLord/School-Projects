# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:26:37 2024

@author: owen.merrill
"""
import random
tries = 0
print("Hello. Would you like to play a guessing game? Yes:1 No:2")
menu = input("Please select your answer: ")
if menu == "2":
    print("Goodbye then.")
if menu == "1":
    goal = random.randint(1, 100)
    done = False
    while done == False:
        guess = input("Guess a number between 1 and 100: ")
        tries = tries + 1
        guess.isdigit()
        if guess.isdigit == True:
            if int(guess) == goal:
                print("You win!")
                done = True
            elif tries >= 7:
                print("You lose. You should get the answer in seven or less tries.")
                done = True
            elif int(guess) < goal:
                print("Too low.")
            elif int(guess) > goal:
                print("Too high.")
        else:
            print("You input an invalid character. Please only use numbers.")
            done = True
else:
    print("Ha ha. Get out.")