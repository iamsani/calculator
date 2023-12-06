choice = int(input("Enter your operation: "))
a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number:"))

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b!=0:
        return a / b
    else:
        return("Cannot divide by ZERO")





if choice == 1:
    result = add(a,b)
    print("result:",result)
elif  choice == 2:
    result = subtract(a,b)
    print("result:",result)
elif choice == 3:
    result = multiply(a, b)
    print("result:", result)
elif choice == 4:
    result = divide(a, b)
    print("result:", result)
else:
    print("Invalid syntax")
