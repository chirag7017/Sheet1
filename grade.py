p = float(input("enter your percentage"))
if p < 25:
    print("your grade is D")
elif p > 25 and p < 45:
    print("your grade is C ")
elif  p > 45 and p < 65:
    print("your grade is B")
elif p > 65 and p < 85:
    print("your grade is A")
else:
    print("your grade is A+")