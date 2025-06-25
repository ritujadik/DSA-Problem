def min_of_two_number(first,second):
    if first > second:
        return (second,"This is a minimum number")
    else:
        return (first,"This is a minimum number")


x = min_of_two_number(5,8)
print(x)

