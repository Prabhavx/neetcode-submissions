class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front, back = [], []
        n = len(nums)
        init = 1
        for i in range(n): front.append(init*nums[i]); init*=nums[i]
        init = 1
        for i in range(n-1,-1,-1): back.append(init*nums[i]); init*=nums[i]
        back = back[::-1]
        ans = [0]*(n)
        ans[0] = back[1]
        ans[-1] = front[-2]

        for i in range(1,n-1):
            ans[i] = front[i-1]*back[i+1]
        
        return ans
        