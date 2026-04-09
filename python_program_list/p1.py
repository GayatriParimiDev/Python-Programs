#This practical states that if the value is positive,negative or zero.

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    

num = int(input("Enter a single whole number: "))
res = check_number(num)
print(f"The number {num} is {res}.")    