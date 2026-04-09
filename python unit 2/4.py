def binary_search(arr, target):
    "Perform binary search on a sorted list"
    low = 0    
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1  

    return -1  


arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = int(input("Enter element to search: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
