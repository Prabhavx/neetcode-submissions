class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0
        for i in range(n):
            if nums[i]==0: start+=1
            else: break
        for i in range(start+1,n):
            if nums[i] == 0: 
                nums[i],nums[start] = nums[start],nums[i]
                start+=1
        end = n-1
        for i in range(n-1,-1,-1):
            if nums[i]==2: end-=1
            else: break
        for i in range(end,-1,-1):
            if nums[i]==2:
                nums[i],nums[end] = nums[end],nums[i]
                end-=1
        