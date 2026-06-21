class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        gmx, gmn = nums[0], nums[0]
        curmax, curmin = 0,0
        tot = 0
        for i in nums:
            curmax = max(curmax+i, i)
            curmin = min(curmin+i, i)
            tot += i
            gmx = max(gmx, curmax)
            gmn = min(gmn, curmin)

        m = max(nums)
        return max(gmx, tot-gmn) if m>0 else m