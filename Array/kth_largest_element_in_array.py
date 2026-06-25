import heapq

class Solution:
    def findKthLargest(self, arr: List[int], k: int) -> int:
        heap = []
        for ele in arr:
            heapq.heappush(heap, ele)
            if(len(heap)>k):
                heapq.heappop(heap)
                
        return heap[0]