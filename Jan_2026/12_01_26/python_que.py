def valid_parenthesis(x):
   new_x = {'}':'{',']':'[',')':'('}
   result = []
   for i in x:
       if i in new_x.values():
           result.append(i)
       elif i in new_x:
           if not result or result.pop() != new_x[i]:
               return False
       else:
           return False

   return not result




x = "({[]})"
print(valid_parenthesis(x))