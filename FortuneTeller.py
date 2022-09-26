def main(): 

    print("Welcome to my Fortune Teller!")
    ColorFortune = input("Pick a color - Red, Blue, Green,: ")

    if ColorFortune in ["Red", "red", "RED"]:
        num = input("Choose a number - 1, 3, 5, 7: ")
        if num == '1':
            print("You will live in a small shack in the middle of nowhere.")
        elif num == '3':
            print("You will be the richest person in the world, but the saddest too")
        elif num == '5':
        #secret fortune
            sf1 = input("69 or 420?: ")
            if sf1 == '69':
                print("You will be constipated for the rest of your life")
            elif sf1 == '420':
                print("You will get the new iPhone 14 Pro!")
        elif num == '7':
            print("You will never be able to eat anything sweet for the rest of your life")
        else:
            print("Choose one of the numbers above.")
    elif ColorFortune in ["Blue", "blue", "BLUE"]:
        num2 = input("Choose a number - 2, 4, 6, 8: ")
        if num2 == '2':
            print("You will own a small potato farm in Wisconsin")
        elif num2 == '4':
        #secret fortune
            sf2 = input("Would you rather have a Benz or a BMW?: ")
            if sf2 == 'Benz' or 'BENZ' or 'benz':
                print("Have fun with your new Benz!")
            elif sf2 == 'BMW' or 'bmw':
                print("Here are there keys, have fun with your new BMW")
        elif num2 == '6':
            print("You will die in war")
        elif num2 == '8':
            print("Tomorrow, you will fart and everyone will hear it.")
        else:
            print("Choose one of the numbers above.")
#write num3 integer input and write last numbers (9, 10, 11, 12).
    elif ColorFortune in ["Green", "green", "GREEN"]:
        num3 = input("Choose a number - 9, 10, 11, 12: ")
        if num3 == '9':
        #secret fortune
            sf3 = input("Do you like Bananas (Yes or No): ")
            if sf3 == 'Yes' or 'yes' or 'YES':
                print("You will live a happy and succesful life. Congrats")
            else:
                print("You will die an early and painful death to the banana army")
        if num3 == '10':
            print("You will age 6 months every day")
        if num3 == '11':
            print("You have to eat dog poop for lunch every 30 days")
        if num3 == '12':
            print("You have the option to choose whether to go to school or not, but you can still go to any ivy league (except for princeton)")

main()
