s = input("Enter a string: ")
result = "".join(dict.fromkeys(s))  
print("String without duplicates:", result)
