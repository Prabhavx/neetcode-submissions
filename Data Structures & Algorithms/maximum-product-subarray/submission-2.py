class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = 1
        mn = 1
        ans = nums[0]
        for i in nums:
            temp = mx*i
            mx = max(i*mx, i*mn, i)
            mn = min(temp,i*mn,i)
            ans = max(ans, mx)
        return ans

