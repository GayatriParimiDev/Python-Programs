def find_max(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_three(a, b, c):
    return find_max(a, max_of_two(b, c))

def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Big number is:", max_of_three(a, b, c))
