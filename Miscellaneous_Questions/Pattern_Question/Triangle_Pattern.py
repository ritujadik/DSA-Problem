def triangle_pattern(n):
    for i in range(1,n):
        for j in range(0,i):
            print(j, end="")
            j+=1
            # ch = chr(ord(ch)+1)


        print()




x = triangle_pattern(5)

