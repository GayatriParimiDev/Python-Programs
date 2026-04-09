#This program is for finding the fibonacci series using recursion.

val = int(input("Enter a value to find it's Fibonacci Series:"))

def fibo(val):
    if val <=0:
        return 0
    elif val == 1:
        return 1
    else:
        return fibo(val-1) + fibo(val-2)
    
for i in range(val):
    print(fibo(i) , end=" ")

