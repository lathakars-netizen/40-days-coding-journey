def calculate(n1,n2,op):
    if op == '+' :
        return n1+n2
    elif op == '-':
        return n1-n2
    elif op == '*':
        return n1*n2
    elif op == '%' and n2 != 0:
           return n1%n2
    else:
         return "error occured"
    
num1,num2 = map(int,input("enter two numbers:").split())
try :
     num1 = float(num1)
     num2 = float(num2)
except ValueError as e:
     print(e)
except ZeroDivisionError as e:
     print(e)
finally :
    print("This is just Crazy!!!")

operation = input("enter the operation('+','-','*','%'):")
result = calculate(num1,num2,operation)

print('-'*11)
print("You got the results")
print("the result is :",result)
    