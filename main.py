firstValue = ''

while firstValue != "quit":
    firstValue = input("Welcome to calculator! Please input the first value, or type 'quit' to end: ")
    signValue = input("Now input the process you want to execute. You can select +, -, *, or / : ")
    secondValue = input("Finally, input the last value: ")

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




