import heapq
from typing import List

def findKthSmallest(arr: List[int], k: int) -> int:
    heap = []
    for item in arr:
        heapq.heappush(heap, -item)
        if(len(heap) > k):
            heapq.heappop(heap)
    return -heap[0]

print(findKthSmallest([20,10,5,9,8],3))