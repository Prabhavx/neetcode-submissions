class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-float('inf')]*(n+1)
        dp[n] = 0
        for i in range(n-1,-1,-1):
            tot = 0
            for j in range(i,min(i+3,n)):
                tot += stoneValue[j]
                dp[i] = max(dp[i], tot-dp[j+1])
        if dp[0]==0: return 'Tie'
        elif dp[0]>0: return 'Alice'
        else: return 'Bob'

        