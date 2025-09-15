def climbup_stairs(x):
    if x<1 or x>45:
        raise ValueError("Input must be in between 1 and 45")

    if x==1 or x ==2:
        return 1
    a,b = 1,2
    for _ in range(3,x+1):
        a,b = b,a+b
    return b



x = 7
print(climbup_stairs(x))
