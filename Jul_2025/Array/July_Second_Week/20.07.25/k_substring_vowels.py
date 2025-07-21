def k_substring_vowel(x,k):
    n = len(x)
    x_new = set('aeiou')
    new_list = []

    count = sum(1 for i in range(k) if x[i] in x_new)
    new_list.append(count)

    for i in range(1,n-k+1):
        if x[i-1] in x_new:
            count-=1
        if x[i+k-1] in x_new:
            count+=1
        new_list.append(count)
    return new_list



x = "workattech"

k = 2
print(k_substring_vowel(x,k))