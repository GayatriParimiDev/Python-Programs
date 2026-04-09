#This program is for finding the factorial of a number using recursion.

num = int(input("Enter a number: "))

def facto(num):
    if num == 0 or num ==1:
        return 1 
    else:
        return num * facto(num-1)
    
print("The Factorial of " , num , "is" , facto(num))
