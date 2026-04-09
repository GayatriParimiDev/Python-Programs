#This program prints elements of a list recursively.

def print_list_recursively(lst):
    if not lst:
        return
    print(lst[0])
    print_list_recursively(lst[1:])

nums = [10, 20, 30, 40]
print_list_recursively(nums)
