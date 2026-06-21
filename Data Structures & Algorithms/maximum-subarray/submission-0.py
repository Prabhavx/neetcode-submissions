class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float('inf')
        sm = 0
        for i in nums:
            sm += i
            if sm <= 0: sm=0
            ans = max(ans, sm)
        m = max(nums)
        return ans if m>0 else m
        