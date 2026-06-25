import math
try :
    number = int(input("enter a number:"))
    result = math.sqrt(number)
    total = math.ceil(result)
    print(total)
except ValueError as e:
    print(e)
finally :
    print("GOT ITT!!")