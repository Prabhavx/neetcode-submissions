class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0]*(m+1) for i in range(n+1)]

        for i in range(1,m+1): dp[0][i] = dp[0][i-1] + 1
        for i in range(1,n+1): dp[i][0] = dp[i-1][0] + 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[j-1] == word2[i-1]: dp[i][j] = dp[i-1][j-1]
                else: dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return dp[n][m] 


#   0 m o n k e y s
# 0 0 1 2 3 4 5 6 7
# m 1 0 1 2 3 4 5 6
# o 2 1 0 1 2 3 4 5
# n 
# e
# y