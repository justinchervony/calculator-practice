firstValue = ''

while firstValue != "quit":
    while True:
        firstValue = input("Welcome to calculator! Please input the first value, or type 'quit' to end: ")
        if firstValue == "quit":
            break
        else:
            try: 
                firstValue = int(firstValue)
                break
            except ValueError:
                print("Please input a number or 'quit'.")
    if firstValue == "quit":
        break
    while True:
        signValue = input("Now input the process you want to execute. You can select +, -, *, or / : ")
        if signValue == '+' or signValue == '-' or signValue == '*' or signValue == '/': 
            break
        else:
            print("Please input one of the four methods listed.")
    while True:
        secondValue = input("Finally, input the last value: ")
        try: 
            secondValue = int(secondValue)
            break
        except ValueError:
            print("Please input a number.")

    firstValue = int(firstValue)
    secondValue = int(secondValue)

    match signValue:
        case "+":
            print (firstValue + secondValue)
        case "-":
            print (firstValue - secondValue)
        case "*":
            print (firstValue * secondValue)
        case "/":
            firstValue = float(firstValue)
            secondValue = float(secondValue)
            print (firstValue / secondValue)




