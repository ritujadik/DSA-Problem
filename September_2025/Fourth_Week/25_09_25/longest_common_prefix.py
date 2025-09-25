def longest_common_prefix(x):
    x.sort()
    first = x[0]
    last = x[-1]
    i = 0
    while i<len(first) and i < len(last) and first[i] == last[i]:
        i+=1

    common_prefix = first[:i]

    return common_prefix



x =  ["flower","flow","flight"]
print(longest_common_prefix(x))