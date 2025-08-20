A = int(input("Enter first number (A): "))
B = int(input("Enter second number (B): "))
C = int(input("Enter third number (C): "))

# Comparing numbers
if A <= B and A <= C:
    print("Minimum number is:", A)
elif B <= A and B <= C:
    print("Minimum number is:", B)
else:
    print("Minimum number is:", C)