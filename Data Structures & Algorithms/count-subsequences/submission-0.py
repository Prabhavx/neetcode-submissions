class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m = len(s)
        n = len(t)
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(m): dp[0][i] = 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[j-1] == t[i-1]: dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else: dp[i][j] = dp[i][j-1]
        
        return dp[n][m]



# Dry running the testcases:

#   0 c a a a t
# 0 1 1 1 1 1 1
# c 0 1 1 1 1 1
# a 0 0 1 2 3 3
# t 0 0 0 0 0 3

#   0 x x y x y
# 0 1 1 1 1 1 1
# x 0 1 2 2 3 3
# y 0 0 0 2 2 5
