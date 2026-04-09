#this program performs binary search on a sorted list.

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

arr = [1,3,5,7,9,11]
x = 7
print("Found at index:", binary_search(arr, x))
