def traingle_pattern(n):
    char = 'A'
    for i in range(0,n):
        for j in range(i):
            print(char,end='')
            char = chr(ord(char)+1)
        print()

x = traingle_pattern(10)