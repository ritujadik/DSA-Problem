def non_repeating_char(x):
    for i in x:
        if x.count(i) == 1:
            return i
    return None




x = "nanu"
print(non_repeating_char(x))


