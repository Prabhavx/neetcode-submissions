class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if len(set(nums)) < n: return True
        else: return False
        