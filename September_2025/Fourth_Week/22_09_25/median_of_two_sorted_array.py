def median_of_two_sorted_array(l1,l2):
    n1 = len(l1)
    n2 = len(l2)
    i,j = 0,0
    x_new = []

    while i<n1 and j<n2:
        if l1[i] <= l2[j]:
            x_new.append(l1[i])
            i+=1
        else:
            x_new.append(l2[j])
            j+=1

    while i<n1:
        x_new.append(l1[i])
        i+=1

    while j<n2:
        x_new.append(l2[j])
        j+=1

    n = len(x_new)
    if n%2!=0:
        median = float(x_new[n//2])

    else:
        mid1 = float(x_new[n//2])
        mid2 = float(x_new[n//2-1])
        median = (mid1 + mid2)/2

    return median




