def missing_number(arr):
    length = len(arr) + 1
    total = length * (length+1) //2

    return  total - sum(arr)



arr = [1,2,3,4,6]
print(missing_number(arr))
