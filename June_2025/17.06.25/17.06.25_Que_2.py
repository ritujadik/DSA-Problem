# Given an integer array, find a maximum product of a triplet in the array

def triplet_product(x):
    x.sort()
    product = 1
    for i in x[-3:-1]:
        product = x[-3]*x[-2]*x[-1]
    return product


x = [2,-3,-6,5,1,4]
print(triplet_product(x))

