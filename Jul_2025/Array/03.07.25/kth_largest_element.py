#kth largest element in an array

def kth_largest_element(x,k):
    x_new = sorted(x,reverse=True)
    return x_new[k-1]



x = [2,3,4,6,1,9]
k = 4
print(kth_largest_element(x,k))