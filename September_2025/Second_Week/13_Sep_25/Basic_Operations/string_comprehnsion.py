def count_string(x):
    if not x:
        return None

    result = []
    count = 1

    for i in range(1,len(x)):
        if x[i] == x[i-1]:
            count+=1
        else:
            result.append(x[i-1] + str(count))
    result.append(x[-1] + str(count))

    compressed = ''.join(result)
    return compressed if len(compressed)<len(x) else x





x = "aabcccccaaa"
print(count_string(x))