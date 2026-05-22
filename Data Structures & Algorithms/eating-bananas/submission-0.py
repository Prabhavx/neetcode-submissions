class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        lo, hi = 1, max(piles)
        ans = int(1e18)
        while lo <= hi:
            mid = (lo+hi)//2
            time = 0
            for i in piles:
                time += -(-i//mid)
            
            if time > h: lo = mid+1
            else: 
                ans = min(ans, mid)
                hi = mid-1

        return ans
        