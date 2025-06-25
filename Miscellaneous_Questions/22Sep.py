y = input("Enter the number")
total = 0
prev_num = 0
x = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for i in y:
    if i in x:
        current_num = x[i]
        if prev_num < current_num:
            total += current_num - 2*prev_num

        else:
            total += current_num

        prev_num = current_num

print("this is the roman value:", total)