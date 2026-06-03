class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(0,2**n):
            s = bin(i)[2:]
            l = []
            s = s.zfill(n)
            for x,j in enumerate(s):
                if j == '1': l.append(nums[x])
            ans.append(l)
        return ans
        