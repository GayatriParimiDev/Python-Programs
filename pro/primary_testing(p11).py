#This is a python program for Primary testing.
# It checks if a number is prime or not.

num = int(input("Enter a positive integer: "))

if num == 0 or num == 1:
    print(f"{num} is neither a prime nor a composite number.")
elif num < 0:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")