def check_num(num):
    if num == 0:       
        print("Number is Zero")
    elif num > 0:     
        if num == 1:
            print("Number is Positive")
        else:
            check_num(num - 1)
    else:             
        if num == -1:
            print("Number is Negative")
        else:
            check_num(num + 1)

num = int(input("Enter a number: "))
check_num(num)
