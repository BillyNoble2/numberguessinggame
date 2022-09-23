
"""
This program selects a random number between the ranges below (1-25 by default), the program will ask the user to guess the number
by inputting some gusses, the program will then provide feedback depending on if the guessed number is correct, higher or lower.
"""
import random
y= (random.randrange(1,25))
while True:
    x=input("Please pick a number ")
    x=int(x)
    x!=y
    if x>y:
        print("the number i'm thiking of is smaller")
    elif x<y:
        print("the number i'm thinking of is larger")
    elif x==y:
        break
print("Good guess! Thanks for playing.")
