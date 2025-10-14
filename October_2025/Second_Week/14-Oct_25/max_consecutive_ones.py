def consecutive_ones(x):
    max_consecutive_ones = 0
    current_count = 0
    for i in x:
        if i == 1:
            current_count += 1
            max_consecutive_ones = max(max_consecutive_ones,current_count)
        else:
            current_count = 0

    return max(current_count,max_consecutive_ones)



x = [1,1,0,1,1,1]
print(consecutive_ones(x))