# how do you create a set
t = {1,3,4}

# how do you add a element in a set
a = {1,2}
a.add(6)
print(a)

# how do we remove a element from set
a = {1,2,3}
a.remove(2)
print(a)

#how do we perform a union,intersection,difference and symmetric difference
a = {1,2,3}
b = {3,4,5}
print(a&b)
print(a|b)
print(a-b)
print(a ^ b)

# how do you check if a set is a subset or superset of another?
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))
print(b.issuperset(a))

# How do you clear all elements from a set?
s = {1,2,3}
s.clear()
print(s)
