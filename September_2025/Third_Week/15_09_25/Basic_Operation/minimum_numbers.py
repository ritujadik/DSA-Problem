def min_num(x):
    i = x[0]
    for j in x:
        if i > j:
            i = j

    return i


x = [2,1,4,5,2,8,9]
print(min_num(x))