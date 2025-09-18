def longest_common_prefix(x):
   if not x:
       return ""

   prefix = x[0]

   for i in x[1:]:
       while not i.startswith(prefix):
           prefix = prefix[:-1]
           if not prefix:
               return ""
   return prefix



x = ["flower","flow","flight"]
print(longest_common_prefix(x))
