def Converter():

    print("Welcome to the measurement converter! By: Eshan Iyer.")
    value = input("Choose your measurement - 1 for feet, 2 for inches, 3 for meters, and 4 for centimeters: ")

    #if value = feet
    
    #if value = inches
    
    #if value = meters
    
    #if value = centimeters
   

    if value == '1':
        conversion = input("Choose your conversion - 2 for inches, 3 for meters, and 4 for centimeters: ")
        if conversion == '2':
            feet = int(input("# of feet here: "))
            inches1 = feet*12
            print("Your Conversion:")
            print(inches1)
        elif conversion == '3':
            feet = int(input("# of feet here: "))
            meters1 = feet/3.281
            print("Your Conversion:")
            print(meters1)
        elif conversion == '4':
            feet = int(input("# of feet here: "))
            centimeters1 = feet*30.48
            print("Your Conversion:")
            print(centimeters1)
        else:
            print("Try again")
    elif value == '2':
        conversion2 = input("Choose your conversion - 1 for feet, 3 for meters, and 4 for centimeters: ")
        if conversion2 == '1':
            inches = int(input("# of inches here: "))
            feet2 = inches/12
            print("Your Conversion:")
            print(feet2)
        elif conversion2 == '3':
            inches = int(input("# of inches here: "))
            meters2 = inches/39.37
            print("Your Conversion:")
            print(meters2)
        elif conversion2 == '4':
            inches = int(input("# of inches here: "))
            centimeters2 = inches*2.54
            print("Your Conversion:")
            print(centimeters2)
        else:
            print("Try again")
    elif value == '3':
        conversion3 = input("Choose your conversion - 1 for feet, 2 for inches, or 4 for centimeters: ")
        if conversion3 == '1':
            meters = int(input("# of meters here: "))
            feet3 = meters*3.281
            print("Your Conversion:")
            print(feet3)
        elif conversion3 == '2':
            meters = int(input("# of meters here: "))
            inches3 = meters*39.37
            print("Your Conversion:")
            print(inches3)
        elif conversion3 == '4':
            meters = int(input("# of meters here: "))
            centimeters3 = meters*100
            print("Your Conversion:")
            print(centimeters3)
        else:
            print("Try again")
    elif value == '4':
        conversion4 = input("Choose your conversion - 1 for feet, 2 for inches, or 3 for meters: ")
        if conversion4 == '1':
            centimeters = int(input("# of centimeters here: "))
            feet4 = centimeters/30.48
            print("Your Conversion:")
            print(feet4)
        elif conversion4 == '2':
            centimeters = int(input("# of centimeters here: "))
            inches4 = centimeters/2.54
            print("Your Conversion:")
            print(inches4)
        elif conversion4 == '3':
            centimeters = int(input("# of centimeters here: "))
            meters4 = centimeters/100
            print("Your Conversion:")
            print(meters4)
        else:
            print("Try again")


        



Converter()