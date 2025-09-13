def search_insert_postion(x,tar):
    for i in range(len(x)):
        if x[i] >= tar:
            return i
    return len(x)



x = [1,3,5,6]
tar = 2
print(search_insert_postion(x,tar))