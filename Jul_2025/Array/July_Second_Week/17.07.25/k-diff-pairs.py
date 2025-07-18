#Given a sorted array A of size n and a number k, return the number of unique pairs which have a difference of k.
def k_diff_pair(x,k):
    seen = set()
    pairs = set()
    for i in range(len(x)):
        if x[i] - k in seen:
            pairs.add((x[i]-k,x[i]))
        if x[i]+ k in seen:
            pairs.add((x[i],x[i]+k))
        seen.add(x[i])

    return len(pairs)

x= [1, 3, 5, 7, 10]
k = 2
print(k_diff_pair(x,k))


