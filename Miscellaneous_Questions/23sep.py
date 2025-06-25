x = ["Flower","Flow","Flight"]
x1 = x.sort()
first = x[0]
last = x[-1]
i = 0
while i<len(first) and i<len(last) and first[i]== last[i]:
    i+=1

common_prefix = first[:i]
print(common_prefix)