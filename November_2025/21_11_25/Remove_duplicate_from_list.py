def remove_duplicate(x):
    new_x = set(x)
    return list(new_x)


x = [1,3,4,5,5,7,9,1,3,2,6,4]
print(remove_duplicate(x))

