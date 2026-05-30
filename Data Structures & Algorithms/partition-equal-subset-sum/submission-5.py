class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        w = sum(nums)
        if w%2 == 1: return False
        else: w//=2
        dp = 1<<0
        for num in nums:
            dp |= dp<<num
        return (dp & (1<<w)!=0)