import random


def NumGen():
    print("Welcome to the random number generator!")
    value = input("Type 1 to start:" )
    if value == '1':
        randinput = int(input("Type a random number between 1 and 100: "))
        rand1 = random.randint(1,100)
        print("Random Number is:")
        print(rand1)
        if randinput == rand1:
            print("Wow, you guessed it!")
        elif randinput < rand1:
            print("You could go higher next time!")
        elif randinput > rand1:
            print("Go lower next time!")
    else:
        print("Restart")
NumGen()