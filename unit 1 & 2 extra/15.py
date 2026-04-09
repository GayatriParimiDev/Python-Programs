def check_and_add(num, step=0):
    if num <= 0:  
        print("Number is not Positive")
        return
    if step == 0:   
        num = num + 2
        print("Positive number after +2 =", num)
    else:
        return
    check_and_add(num, step + 1)  

num = int(input("Enter a number: "))
check_and_add(num)
