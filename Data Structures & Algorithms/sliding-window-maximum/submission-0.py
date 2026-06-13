import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = [(-j,i) for i,j in enumerate(nums[:k])]
        heapq.heapify(heap)
        ans = [-heap[0][0]]

        for i in range(k,n):
            l = i-k+1
            r = i
            heapq.heappush(heap, (-nums[r],r))
            while heap[0][1] < l: heapq.heappop(heap)
            ans.append(-heap[0][0])
        
        return ans
