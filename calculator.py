a=float(input("enter a number:"))
b=float(input("enter another number:"))
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Division by zero is not possible"

print("sum of these numbers is:",add(a,b))
print("difference of these numbers is:",subtract(a,b))
print("product of these numbers is:",multiply(a,b))
print("quotient of these numbers is:",divide(a,b))