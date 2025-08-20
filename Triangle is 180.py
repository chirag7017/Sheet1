a = int(input("enter angle a "))
b = int(input("enter angle b "))
c = int(input("enter angle c "))

if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("the tringle is valid")
else:
    print("the triangle is not valid")