def most_frequent_element(x):
    result = None
    max_count = 0
    for i in range(len(x)):
        count = 1
        for j in range(i+1,len(x)):
            count += 1
        if count>max_count:
            max_count = count
            result = x[i]
    return result


x = [4,3,2,4,3,4,4,4,1]
print(most_frequent_element(x))