class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            if nums[i]>n or nums[i]<=0: i+=1; continue
            ind = nums[i]-1
            if nums[i]!=nums[ind]:
                nums[i],nums[ind] = nums[ind],nums[i]
            else: i+=1

        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
