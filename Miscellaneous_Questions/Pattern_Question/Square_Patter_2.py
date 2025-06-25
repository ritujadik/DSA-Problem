def square_pattern(n):
    num = 1
    for i in range(0,n):
        for j in range(0,n):
            print(num,'',end='')
            num+=1

        print()

x = square_pattern(5)
