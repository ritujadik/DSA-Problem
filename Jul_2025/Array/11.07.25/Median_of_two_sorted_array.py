def median(num1,num2):
    x = []
    x = num1 + num2
    x.sort()
    n = len(x)
    if n%2!=0:
        r = n//2
        print(r)
        return(x[r])
    else:
        r1 = n//2
        r2 = r1-1
        return (x[r1]+x[r2])/2



num1 = [2,4,5]
num2 = [3]
print(median(num1,num2))


# def search_position(x,tar):
#     for i in range(len(x)):
#         if x[i] == tar:
#             return (i)


# def binary_search(x,tar):
#     left,right = 0,len(x)-1
#     while left<right:
#         mid = (left + right)//2
#         if x[mid] == tar:
#             return mid
#         elif x[mid]<tar:
#             left = mid + 1
#         else:right = mid-1
#     return -1
#
# x = [2,3,4,5,9]
# print(binary_search(x,tar=5))

