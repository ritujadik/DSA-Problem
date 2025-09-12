def flattend_list(x):
    flat = []
    for i in x:
        for j in i:
            flat.append(j)

    return flat


x = [[1, 2], [3, 4], [5, 6]]
print(flattend_list(x))
