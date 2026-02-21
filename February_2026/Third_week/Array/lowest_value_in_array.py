def lowest_value(arr):
    lowest_val = arr[0]
    for i in arr:
        if i<lowest_val:
            lowest_val = i

    return lowest_val


arr = [3,1,4,5,7,5,9]
print(lowest_value(arr))