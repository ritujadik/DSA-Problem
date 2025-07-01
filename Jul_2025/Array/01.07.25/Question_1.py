# we have given an array where we need to show the index and its value

# arr = [9,4,5,6,3,8,2]
# for i,j in enumerate(arr):
#     print(f"index:{i},value:{j}")

# Given a list of integer,find the element that appears most frequently

def most_frequent(x):
    frequency = []
    values = []
    for i in range(len(x)):
        found = False
        for j in range(len(values)):
            if x[i] == values[j]:
                frequency[j] +=1
                found = True
                break
        if not found:
            values.append(x[i])
            frequency.append(1)
    max_index = 0
    for i in range(1,len(frequency)):
        if frequency[i] > frequency[max_index]:
            max_index = i

    return values[max_index]




x = [4,5,6,4,4,4,5,6,6,4,6]
print(most_frequent(x))