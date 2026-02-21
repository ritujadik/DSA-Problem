def duplicates(x):
    seen = {}
    new_arr = []
    for i  in x:
        if i in seen:
            seen[i]+=1
            if seen[i]  == 2:
                new_arr.append(i)
        else: seen[i]=1
    return new_arr


x = [4, 3, 2, 7, 8, 2, 3, 1,1,1]
print(duplicates(x))
