def print_range(num, end):
    if num < end:  
        return
    print(num)
    print_range(num - 4, end)  

start = -4
end = -40
print_range(start, end)
