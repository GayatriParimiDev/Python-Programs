num = int(input("Enter a number: "))
def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n-1)

print(f"Sum of numbers from 1 to {num} is {recursive_sum(num)}")
