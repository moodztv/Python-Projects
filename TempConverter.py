def tempconverter():

    print("Welcome to the temperature converter! Made by: Eshan Iyer.")
    value = input("Choose your temperature measurement: 1 for Fareinheit or 2 for celsius: ")

    if value == '1':
        Fdegr = int(input("Input temperature Fareinheit here: "))
        Celsius = Fdegr - 32 
        print("° Celsius:")
        print(Celsius)
    elif value == '2':
        Cdegr = int(input("Input temperature Celsius here: "))
        Fareinheit = Cdegr * 1.8 + 32
        print("° Fareinheit:")
        print(Fareinheit)
    else:
        print("Try again")
tempconverter()