#Given 2 sorted arrays, return the intersection of both the arrays.
# The intersection of 2 arrays means all the elements which are present in both.

def intersection_of_two_sorted_array(x,y):
   i = j = 0
   result = []
   while i < len(x) and j < len(y):
       if x[i] == y[j]:
           result.append(x[i])
           i+=1
           j+=1
       elif x[i]<y[j]:
           i+=1
       else:j+=1
   return result

x = [1,2,3,3,4,4,4,5,]
y = [3,3,3,4,4,4,5]
print(intersection_of_two_sorted_array(x,y))

