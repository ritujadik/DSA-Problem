input = "a1b3c4d1a2"
x1 = []
x2 = []
for i in range(0,len(input),2):
    x1.append(input[i])
    x2.append(int(input[i+1]))
for j in range(len(x1)):
    for _ in range(x2[j]):
        print(x1[j],end="")








