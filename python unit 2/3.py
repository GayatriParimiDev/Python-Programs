def print_list_recursive(lst, index=0):
    "Recursively print elements of a list"
    if index == len(lst):  
        return
    print(lst[index])
    print_list_recursive(lst, index + 1)   

data = [10, 20, 30, 40, 50]
print("List elements:")
print_list_recursive(data)
