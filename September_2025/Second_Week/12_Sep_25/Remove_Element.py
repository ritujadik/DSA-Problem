def remove_element(x,val):
    i = 0
    for j in range(len(x)):
        if x[j] != val:
            x[i] = x[j]
            i+=1
    return i




x = [3,2,2,3,4,5,5,9,9]
val = 9
print(remove_element(x,val))