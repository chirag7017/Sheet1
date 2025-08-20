a = int(input("enter the angle"))
b = int(input("enter the angle"))
c = int(input("enter the angle"))
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    if a == 90 or b== 90 or c == 90:
        print("Right Triangle")
    elif a > 90 or b > 90 or c > 90:
        print("Obtuse Trinagle")
    else:
        print("Acute Triangle")
else:
    print("Invalid angles")