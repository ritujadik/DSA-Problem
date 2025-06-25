# we have to move all the zero's in the last in an given array if there is no zero element than array should be same
def move_zeros_to_end(x):
    pos = 0
    for i in range(len(x)):
        if x[i] != 0:
            x[pos] = x[i]
            pos +=1
    for i in range(pos,len(x)):
        x[i] = 0


x = [2,3,0,1,9,0,8,7]
move_zeros_to_end(x)
print(x)