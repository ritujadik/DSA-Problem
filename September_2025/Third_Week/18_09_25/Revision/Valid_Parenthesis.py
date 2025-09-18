def valid_parenthesis(x):
    new_pair = {'}':'{',']':'[',')':'('}
    pairs = []

    for i in x:
        if i in new_pair.values():
            pairs.append(i)

        elif i in new_pair:
            if not pairs or pairs[-1] != new_pair[i]:
                return False

            pairs.pop()

        else:
            continue

    return True if not pairs else False


x = "{{[}}"
print(valid_parenthesis(x))
