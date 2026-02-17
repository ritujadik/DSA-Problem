# example of shallow copy
# Answer-shallow copy when we copy the original object and if we do the changes in the copied object except the nested one in the same that would not impact the orignal object
# but if we do the changes in the nested object of the copied object that changes would be happen in the orignal object also as both the object
#orignal and copied will refer the same memory allocation for the nested object.
import copy

# x = ["apple","mango",["guava","grapes"]]
# y = x.copy()
#
# y.append("banana")
#
# print(y)
# print(x)

# deep copy- make the copy of the orignal object including nested one at the different memory space
# so if we do the changes in nested object of the copied object that would not impact the nested object of the original object
# example of deep copy
x = ["apple","mango",["guava","grapes"]]
y = copy.deepcopy(x)

y[2][0] = "banana"
print(y)
print(x)