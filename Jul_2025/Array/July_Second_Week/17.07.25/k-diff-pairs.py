#Given a sorted array A of size n and a number k, return the number of unique pairs which have a difference of k.

def k_diff(x,k):
    left,right = 0,1
    count = 0
    seen_pairs = set()
    n = len(x)
    while right < n:
        if left == right:
            right += 1
            continue
        diff = x[right] -x[left]

        if diff < k:
            right+=1
        elif diff > k:
            left+=1
        else:
            pair = (x[left],x[right])
            if pair not in seen_pairs:
                seen_pairs.add(pair)
                count+=1
            left+=1
            right+=1
    return count

y = k_diff([1,3,5,7,10],2)
print(y)
