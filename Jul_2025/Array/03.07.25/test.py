def lanrgest_substring(x):
    max_length = 0
    temp_max = 0
    new_li = []
    for i in range(len(x)):
        if x[i] not in new_li:
            new_li.append(x[i])
            temp_max+=1
            max_length = max(max_length,temp_max)
        else:
            idx = new_li.index(x[i])
            new_li = new_li[idx+1:]
            new_li.append(x[i])
            temp_max = len(new_li)

    return max_length

x = "abcabcabc"
print(lanrgest_substring(x))