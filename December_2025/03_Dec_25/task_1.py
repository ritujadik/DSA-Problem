def findthepasswordcomplexity(password):
    n = len(password)
    symbol = '[]!@$%^&&(()_+&^{[]}_+'
    count = 0
    if n < 6:
        count+=0
    elif n>=6 and n<=10:
        count+=1
    elif n>10:
        count+=2

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in symbol for c in password)

    if has_lower:
        count+=1

    if has_upper:
        count+=1

    if has_digit:
        count+=1

    if has_symbol:
        count+=2

    return count



password ="heLloworld"
print(findthepasswordcomplexity(password))

