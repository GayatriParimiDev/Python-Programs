# This program generates Fibonacci strings where the first two strings are "A" and "B".

def fibonacci_strings(n):
    if n == 1:
        return "A"
    elif n == 2:
        return "B"
    else:
        return fibonacci_strings(n-1) + fibonacci_strings(n-2)

for i in range(1, 6):
    print(fibonacci_strings(i))
