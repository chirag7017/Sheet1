a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))

if a >= b and a>= c:
    print("Maximum number is:",a)
elif b >= a and b >=c :
    print("Maximum number is:",b)
else:
    print("Maximum number is:",c)