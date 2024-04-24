# 1
try:
    num=40/0
    number=int(input("Enter the input value"))
    print(number)
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print("Invalid input")
