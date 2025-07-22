#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).
#steps we have to taken
#1.we have to merge both the arrays in a sorted way
#2.we have to check the length of the merged array
#3.we have to find out the median on the basis of the number of elements in a merged array

def mediaon_of_two_sorted_array(nums1,nums2):
    i = j = 0
    merged_new = []
    n1 = len(nums1)
    n2 = len(nums2)
    while i < n1 and j < n2:
     if nums1[i]<=nums2[j]:
         merged_new.append(nums1[i])
         i+=1
     else:
         merged_new.append(nums2[j])
         j+=1

    while i<n1:
        merged_new.append(nums1[i])
        i+=1
    while j<n2:
        merged_new.append(nums2[j])
        j+=1
    new_len = len(merged_new)
    if new_len%2!=0:
        median = merged_new[new_len//2]
    else:
        mid1 = merged_new[new_len//2-1]
        mid2 = merged_new[new_len//2]
        median = (mid1+mid2)/2

    return median



nums1 = [1,2]
nums2 = [3,4]
print(mediaon_of_two_sorted_array(nums1,nums2))
