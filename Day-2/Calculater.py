operator = input("Enter an Operator (+, -, *, /): ")
num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

if operator == "+":
    result = num1 + num2
    print(result)
    
elif operator == "-":
    result = num1 - num2
    print(result)
    
elif operator == "*":
    result = num1 * num2
    print(round(result))
    
elif operator == "/":
    result = num1 / num2
    print(result)            
else:
    print("Not valid")    