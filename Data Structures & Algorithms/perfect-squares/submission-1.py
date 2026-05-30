class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        sq = int(n**0.5)
        for i in range(1,n+1):
            for j in range(1,sq+1):
                if j*j<=i: dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[n]
        