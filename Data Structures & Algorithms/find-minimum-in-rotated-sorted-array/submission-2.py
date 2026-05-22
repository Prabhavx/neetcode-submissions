class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        ans = 1001
        
        while lo<=hi:
            if hi-lo==1: ans = min(ans, nums[lo], nums[hi])
            mid = (lo+hi)//2

            if nums[lo] < nums[mid] < nums[hi]: ans=min(ans, nums[lo]); hi = mid-1
            elif nums[lo] > nums[mid] > nums[hi]: ans=min(ans, nums[hi]); lo = mid+1
            elif nums[lo] < nums[mid] > nums[hi]: ans=min(ans, nums[lo]); lo = mid+1
            else: ans=min(ans, nums[mid]); hi = mid-1
        
        return ans