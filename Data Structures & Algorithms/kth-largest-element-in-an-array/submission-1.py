import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k,n):
            if nums[i]<heap[0]: continue
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
        
        return heap[0]
                
        