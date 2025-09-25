def rom_to_int(x):
    x_new = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1
    }

    total = 0
    prev_num = 0
    for i in x:
        if i in x_new:
            temp = x_new[i]

            if prev_num<temp:
                total+=temp-2*prev_num
            else:
                total+=temp

            prev_num = temp

    return total


x = "IX"
print(rom_to_int(x))