#This practical states that ffind the table of the given number.

def print_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

num = int(input("Enter a number to print its table: ") )

print_table(num)
