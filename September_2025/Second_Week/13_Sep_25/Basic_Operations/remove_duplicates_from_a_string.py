def remove_duplicate_char(x):
    result = ''
    for i in x:
        if x.count(i) == 1:
            result+=i

    return result




x = "nanu"
print(remove_duplicate_char(x))