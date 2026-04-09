#This program is for using the lambda function to find the addition , subtraction and multiplication operation.

def add(x , y):
    return x + y

def sub(x , y):
    return x - y    

def mul(x , y):
    return x * y

print("Select operation.")
print("1.Addition") 
print("2.Subtraction")
print("3.Multiplication")
choice = input("Enter choice(1/2/3):")

if choice not in ('1','2','3'):
    print("Invalid Input")
else:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if choice == '1':
        sum = lambda num1,num2 : num1 + num2
        print(add(num1,num2))
    elif choice == '2':
        sub = lambda num1,num2 : num1 - num2
        print(sub(num1,num2))
    elif choice == '3':
        mul = lambda num1,num2 : num1 * num2