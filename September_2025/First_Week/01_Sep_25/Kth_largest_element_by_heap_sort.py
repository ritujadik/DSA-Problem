import heapq


def kth_largest_element(nums,k):
    new_heap = []

    for i in nums:
        heapq.heappush(new_heap,i)

        if len(new_heap)>k:
            heapq.heappop(new_heap)

    return new_heap[0]



nums = [6,3,2,4,8,1,9]
k = 5
result = kth_largest_element(nums,k)
print(result)