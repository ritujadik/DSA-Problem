def valid_parenthesis(x):
    x_new = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    pairs = []

    for i in x:
        if i in x_new.values():
            pairs.append(i)

        elif i in x_new:
            if not pairs or pairs[-1] != x_new[i]:
                return False

            pairs.pop()

        else:continue

    return True if not pairs else False

x = "[]{}()"
print(valid_parenthesis(x))