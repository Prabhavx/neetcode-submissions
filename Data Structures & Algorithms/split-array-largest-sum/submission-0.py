class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lo, hi = max(nums), sum(nums)

        while lo<=hi:
            mid = (lo+hi)//2

            split = 1
            bag = 0
            for i in nums:
                if bag+i > mid:
                    bag = i
                    split+=1
                else: bag+=i
            
            if split > k: lo = mid+1
            else: hi = mid-1
        
        return lo