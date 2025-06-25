def patternquestion(n):
    ch = 'A'
    for i in range(0,n):
        for j in range(1,n+1):
            print(ch,"",end="")
            ch = chr(ord(ch) + 1)
        print()





x = patternquestion(4)
