import random


def diceroller():

    print("Welcome to the dice roller!")
    value = input("Enter 1 to roll the dice!: ")

    if value == '1':
        dice1 = random.choice(['1','2','3','4','5','6'])
        dice2 = random.choice(['1','2','3','4','5','6'])

    print("Result:")
    print("Dice 1: "+dice1)
    print("Dice 2: "+dice2)



diceroller()