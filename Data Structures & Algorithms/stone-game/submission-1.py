class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*n for i in range(n)]
        for i in range(n): dp[i][i] = piles[i]

        for le in range(1,n):
            for i in range(n-le):
                j = i+le
                dp[i][j] = abs(dp[i][j-1]-piles[j])
        return dp[0][n-1]>0

