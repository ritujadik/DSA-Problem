# Most frequent item

def most_frequent_item(x):
    freq = {}
    for i in x:
        freq[i] = freq.get(i, 0) + 1
    max_num = max(freq,key=freq.get)

    return max_num



x = [4,5,6,6,4,5,6,6,4,6]
print(most_frequent_item(x))