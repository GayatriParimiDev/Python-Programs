#This is a Fibonacci sequence generator.

n = int(input("Enter the number of Fibonacci terms to print: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
