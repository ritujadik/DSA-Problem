def maximum_number(x):
    i = x[0]
    for j in x:
        if i<j:
            i = j
    return i


x = [2,3,9,8,10]
print(maximum_number(x))