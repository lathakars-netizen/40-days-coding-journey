a,b,c = map(int,input("enter the three numbers : ").split())
if a>b and a>c : 
    print(a," is the largest number")
elif b>a and b>c :
    print(b," is the largest number")
else :
    print(c," is the largest number")