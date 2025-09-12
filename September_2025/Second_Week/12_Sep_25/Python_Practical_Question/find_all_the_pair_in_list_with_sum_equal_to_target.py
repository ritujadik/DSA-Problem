def sum_equal_to_tar(x,k):
    seen = set()
    result = set()

    for i in x:
        tar = k - i
        if tar in seen:
            result.add(tuple(sorted((i,tar))))
        seen.add(i)

    return list(result)


x = [1, 2, 3, 4, 5]
k = 6
print(sum_equal_to_tar(x,k))


