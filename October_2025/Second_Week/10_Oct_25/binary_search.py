"""
binary search in python
"""
def binary_search(arr,tar):
    left = 0
    right = len(arr)-1

    while left<= tar:
        mid = left + (right-left)//2

        if arr[mid] == tar:
            return mid

        elif arr[mid]>tar:
            right = mid-1

        else:
            left = mid+1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tar = 7
result = binary_search(arr,tar)

if result !=-1:
    print(f"element found at index {result}")
else:
    print("element not found")


