class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        h = 0
        ans = nums[0]
        for i in range(n):
            if nums[i] == ans: h+=1
            else:
                if h>0: h-=1
                else:
                    ans = nums[i]
                    h = 1
        return ans
