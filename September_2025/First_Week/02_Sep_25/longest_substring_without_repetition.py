def longest_substring(x):
    count = 0
    new_x = []
    left = 0
    max_count = 0
    for i in range(len(x)):
        if x[i] not in new_x:
            new_x.append(x[i])
            count+=1
        else:
            while x[left] != x[i]:
                new_x.pop(0)
                left+=1
            left+=1

        max_count = max(max_count,count)
    return max_count


y = "pwwkew"
print(longest_substring(y))