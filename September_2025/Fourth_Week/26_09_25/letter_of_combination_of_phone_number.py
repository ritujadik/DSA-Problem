def phone_number(x):
    x_new = {
        "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
    }
    result = [""]
    for i in x:
        if i in x_new.keys():
            letters = x_new[i]
            result = [prefix + letter for prefix in result for letter in letters]

    return result


x = "23"
print(phone_number(x))