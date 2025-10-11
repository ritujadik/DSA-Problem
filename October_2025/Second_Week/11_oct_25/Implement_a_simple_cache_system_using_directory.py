class SimplecCache:
   def __init__(self):
       self.cache = {}

   def get(self,key):
       return self.cache.get(key,"not found")

   def set(self,key,value):
       self.cache[key] = value


cache = SimplecCache()
cache.set("name","Alice")
print(cache.get("name"))
print(cache.get("age"))