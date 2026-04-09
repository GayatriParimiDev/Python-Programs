#This practical states that we need to find the biggest of three numbers.

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
val = int(input("Enter the first number: "))
val1 = int(input("Enter the second number: "))
val2 = int(input("Enter the third number: "))

result = find_largest(val, val1, val2)
print(f"The largest number among {val}, {val1}, and {val2} is {result}.")