x = [1,2,3,4,5,8,9,6,7]
k = 4

length = len(x)
print(length)
y = length - k
print(y)
result = []
for i in range(0,length,k):
        if i + k <= length:
            result.append(x[i:i+k][::-1])
        else:
            result.extend(x[i:])

print(result)
