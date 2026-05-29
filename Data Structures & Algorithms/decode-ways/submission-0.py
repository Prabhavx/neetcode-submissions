class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0

        n = len(s)
        dp = [[0,0] for _ in range(n)]
        dp[0][0] = 1

        for i in range(1,n):
            if s[i] == '0': 
                if s[i-1]<='2': dp[i][1] = dp[i-1][0]
                else: return 0
            elif s[i-1]+s[i] <= '26':
                dp[i][0] = dp[i-1][0] + dp[i-1][1]
                dp[i][1] = dp[i-1][0]
            else:
                dp[i][0] = dp[i-1][0] + dp[i-1][1]

        return dp[n-1][0] + dp[n-1][1]

                

        