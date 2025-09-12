def rotate_kth_elem(x,k):
    k = k%len(x)
    return x[k:] + x[:k]





x = [1, 2, 3, 4, 5]
print(rotate_kth_elem(x, 2))

