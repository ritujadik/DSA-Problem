def remove_duplicate(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y



x = [1,2,3,2,1,3,5]
print(remove_duplicate(x))