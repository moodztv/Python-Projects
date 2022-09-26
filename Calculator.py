def MyCalculator():

    print("Welcome to Eshan's Calculator")

    opr = int(input("Choose an operation - 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: "))

    num1 = int(input("Enter your first number here: "))
    num2 = int(input("Enter your second number here: "))

    if opr == 1:
        result = num1 + num2
        print(result)
    if opr == 2:
        result = num1 - num2
        print(result)
    if opr == 3:
        result = num1 * num2
        print(result)
    if opr == 4:
        result = num1 / num2
        print(result)

MyCalculator()