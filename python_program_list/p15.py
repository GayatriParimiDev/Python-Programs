#This program is to find the sum of natural numbers using recursion.

num = int(input("Enter a value to find it's sum of natural numbers: "))

def sumition(num):
    if num <= 1:
        return num
    else:
        return num + sumition(num-1)
    
print("The sum of " , num , "Natural Numbers is: " , sumition(num))