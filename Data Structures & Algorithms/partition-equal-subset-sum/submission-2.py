class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        w = sum(nums)
        n = len(nums)
        if w%2 == 1: return False
        else: w//=2
        dp = [[0]*(w+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(w+1):
                if nums[i-1]>j: dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-nums[i-1]]+nums[i-1])
        return dp[n][w] == w