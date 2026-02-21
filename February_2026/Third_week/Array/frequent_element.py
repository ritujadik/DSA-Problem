def most_frequent_element(arr):
    frequent = {}
    for i in arr:
        if i in frequent:
            frequent[i]+=1
        else:
            frequent[i] = 1
    return max(frequent.keys(), key=frequent.get)


arr = [1, 3, 2, 1, 2, 2, 3, 3, 3,2,1,2]
print(most_frequent_element(arr))