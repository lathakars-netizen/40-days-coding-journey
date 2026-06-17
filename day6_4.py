def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "division can't be possible"
    else:
        return x%y
    
def calculator():
    print("----CALCULATOR----")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    while True :
        choice = input("\nEnter choice (1-5): ")
        if choice == '1':
            num1= int(input(print("enter num1:")))
            num2 = int(input(print("enter num2:")))
            print("the sum of two numbers:",add(num1,num2))
        elif choice == '2':
            num1= int(input(print("enter num1:")))
            num2 = int(input(print("enter num2:")))
            print("the subtraction of two numbers:",subtract(num1,num2))
        elif choice == '3':
            num1= int(input(print("enter num1:")))
            num2 = int(input(print("enter num2:")))
            print("the multiplication of two numbers:",multiply(num1,num2))
        elif choice == '4':
            num1= int(input(print("enter num1:")))
            num2 = int(input(print("enter num2:")))
            print("the division of two numbers:",divide(num1,num2))
        else:
            print("invalid input")
    print("exit , good bye")
calculator()