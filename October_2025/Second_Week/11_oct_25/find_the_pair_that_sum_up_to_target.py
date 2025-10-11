def find_pair(arr,tar):
    seen = set()
    for i in arr:
        complement = tar-i
        if complement in seen:
            return (complement,i)

        seen.add(i)

    return None


arr = [2,7,11,15]
target = 9

print(find_pair(arr,target))
