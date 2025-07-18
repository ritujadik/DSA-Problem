# Given two sorted arrays A and B, and another value k, print the kth element of the resultant sorted array.

def two_sorted_arrays(x,y,k):
    result = []
    i = j = 0

    while i<len(x) and j<len(y):
        if x[i]<y[j]:
            result.append(x[i])
            i+=1
        else:
            result.append(y[j])
            j+=1
    while i<len(x):
        result.append(x[i])
        i+=1
    while j<len(y):
        result.append(y[j])
        j+=1

    return result[k-1]



x = [1,2,2,3,4]
y = [2,3,3,4,4,5]
print(two_sorted_arrays(x,y,3))


