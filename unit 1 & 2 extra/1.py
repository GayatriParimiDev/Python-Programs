a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed!"
    return a / b

print("Addition:", add(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
