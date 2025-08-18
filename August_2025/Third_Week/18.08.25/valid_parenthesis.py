"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def valid_parenthesis(x):
    new_pair = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    pairs = []

    for char in x:
        if char in new_pair.values():
            pairs.append(char)
        elif char in new_pair:
            if not pairs or pairs[-1] !=new_pair[char]:
                return "Invalid Parenthesis"
            pairs.pop()
        else:
            continue
    return "valid parenthesis" if not pairs else "Invalid parenthesis"

x = "]{}()["
print(valid_parenthesis(x))