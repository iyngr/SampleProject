import os, sys


# import on separate lines, while importing multiple use csv
# from module_name import package1, package2, package3

def func(one, two,
         three, four,
         five, six):
    print("Hello")


# Add two lines between top level functinos and top level classes.

a = [1, 2,
     3, 4,
     5, 6]
# the ending square brace should be in the same line as the last element in the array or list When using PEP
# Guidelines follow along in the PyCHarm settings -> Code Style -> Python -> 4 whitespaces and indentation
# Do not add whitespaces when referring variables or arguments in a function. SUch as list [ a ] and func( a )
# Separate the operations based on priority such as Arithmetic operations in one line.
# if statements to be separated after the : and the result after the condition to be in another line.
# Calling multiple functions do it on different line do not cram them all into one line.

# While Loop additional handlers
import random


playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp )

    if playerhp == 30:
        print("You're dead. You cannot re spawn. You've been teleported to Hospital")
        break

# Classes and Objects

