import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        n = len(stones)
        if n==1: return -stones[0]
        while n>1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x==y: 
                n-=2
            else:
                heapq.heappush(stones, y-x)
                n-=1
        if n==0: return 0
        return -stones[0]

