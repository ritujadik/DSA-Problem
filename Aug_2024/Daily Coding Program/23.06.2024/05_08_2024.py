def myfunction(str):
    s = []
    max_string = []

    for i in str:
        if i in s:
            s = s[s.index(i)+1:]
        s.append(i)

        if len(s)>len(max_string):
            max_string = s.copy()
    return (len(max_string))

newarr = "pwwkew"
newarr1 = myfunction(newarr)
print(newarr1)
