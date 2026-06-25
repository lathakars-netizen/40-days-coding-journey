#a,b = map(int,input("enter a number:").split())
#try :
#   print("result:",a/b)
#except ZeroDivisionError as e:
#   print("error found",e)

try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Zero is not allowed.")