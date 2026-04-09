#This program checks if a number is a perfect number.

def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"{num} is Perfect? {is_perfect(num)}")
