#This program is to find the power of a number using recursion.

bs = int(input("Enter the base value: "))
pw = int(input("Enter the power value for the base value: "))

def pow(bs , pw):
    if pw == 0:
        return 1
    else:
        return bs * pow(bs , pw-1)
    
print("The Vlue of ", bs , "to the  power of ", pw , "is: " ,pow(bs,pw))