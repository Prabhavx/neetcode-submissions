class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        lo, hi = max(weights), sum(weights)
        while lo<=hi:
            mid = (lo+hi)//2
            req = 0
            weigh = 0
            for i in range(n):
                weigh += weights[i]
                if weigh > mid: 
                    weigh = weights[i]
                    req+=1
            if req < days: hi = mid-1
            else: lo = mid+1
        return lo
        