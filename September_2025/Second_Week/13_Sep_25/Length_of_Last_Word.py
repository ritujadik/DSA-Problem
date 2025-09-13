def length_of_last_word(x):
    x_new = x.split()
    lengths = [len(word) for word in x_new ]
    print(lengths[-1])



x = "Hello World"

print(length_of_last_word(x))