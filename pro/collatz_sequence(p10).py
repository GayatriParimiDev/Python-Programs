# This is a program to generate the Collatz sequence for a given number.

n = int(input("Enter a number: "))
while n != 1:
    print(n, end=",")
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
print(1)  