class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        strt = n-1
        for i in range(n-1,-1,-1):
            if nums[i]==val: strt-=1
            else: break
        for i in range(strt,-1,-1):
            if nums[i]==val:
                nums[i],nums[strt] = nums[strt],nums[i]
                strt-=1
        return strt+1
        