class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=3: return max(nums)

        dp1 = [[0,0] for _ in range(n)]
        dp2 = [[0,0] for _ in range(n)]  
        
        dp1[0][0] = nums[0]
        dp2[1][0] = nums[1]

        for i in range(1,n-1):
            dp1[i][0] = dp1[i-1][1] + nums[i]
            dp1[i][1] = max(dp1[i-1][1], dp1[i-1][0])

        for i in range(2,n):
            dp2[i][0] = dp2[i-1][1] + nums[i]
            dp2[i][1] = max(dp2[i-1][1], dp2[i-1][0])
        
        
        return max(dp2[n-1][0], dp2[n-1][1], dp1[n-2][0], dp1[n-2][1])