# Given two sorted array A and B.find the merged sorted array C by merging A and B

def two_sorted_array(A,B):
    C = []
    i = j = 0

    while i < len(A) and j<len(B):
        if A[i]<B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1

    while i<len(A):
        C.append(A[i])
        i+=1
    while j<len(B):
        C.append(B[j])
        j+=1
    return C



A = [1,2,3,4,5]
B=[2,4,5,5]
print(two_sorted_array(A,B))