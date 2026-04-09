#This practical states that to find dthe sum of the given value.

def find_sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

val = int(input("Enter a number to find the sum of all numbers up to it: "))

result = find_sum(val)
print(f"The sum of all numbers from 1 to {val} is {result}.")