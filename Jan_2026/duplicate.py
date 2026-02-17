def freq_each_elem(x):
    freq = {}
    for i in x:
        if i in freq:
            freq[i]+=1

        else:
            freq[i]=1
    max_freq = max(freq.values())
    result = []

    for k in freq:
        if freq[k] == max_freq:
            result.append(k)

    return result,max_freq





x = [1,9,7,3,6,6,5,5,2,5,1,1,2]
print(freq_each_elem(x))