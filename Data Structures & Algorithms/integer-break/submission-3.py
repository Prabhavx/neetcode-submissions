class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0,0,2,3]
        if n==3: return 2
        if n==2: return 1
        for i in range(4,n+1):
            dp.append(max(dp[i//2]*dp[i-i//2],dp[i//2-1]*dp[i-i//2+1]))
        return dp[n]