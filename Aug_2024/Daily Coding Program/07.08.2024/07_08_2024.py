def myfunction(input_str):
    new_obj = {}
    arr = []
    missing_arr1 = []
    missing_arr2 = []
    missing_arr3 = []

    for i in input_str:
        if i in new_obj:
            new_obj[i] += 1
        else:
            new_obj[i] = 1

    sorted_new_obj = dict(sorted(new_obj.items(), key=lambda x: x[1], reverse=True))

    for index, i in enumerate(sorted_new_obj):
        if index < 8:
            arr.append(i)
        elif 8 <= index < 16:
            missing_arr1.append(i)
        elif 16 <= index < 24:
            missing_arr2.append(i)
        else:
            missing_arr3.append(i)


    total_sum = 0

    for char in arr:
        total_sum += new_obj[char] * 1

    for char in missing_arr1:
        total_sum += new_obj[char] * 2

    for char in missing_arr2:
        total_sum += new_obj[char] * 3

    for char in missing_arr3:
        total_sum += new_obj[char] * 4


    return total_sum








input_str = "ebsgijykaqhxtouwmdrfplz"
total_sum = myfunction(input_str)
print(total_sum)



