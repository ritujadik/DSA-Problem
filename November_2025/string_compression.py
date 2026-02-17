"string compression"

def string_compression(x):
    new_x = {}
    for i in x:
        new_x[i] = new_x.get(i,0)+1

    compressed = ""
    for char,count in new_x.items():
        compressed += f"{char}{count}"
    return compressed



x = "aaabb"
print(string_compression(x))

