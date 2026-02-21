def findSecondLar(arr):
    arr.sort()
    return arr[-2]



arr = [2,9,7,1,6,8]
print(findSecondLar(arr))
