class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        nums.insert(0,1); nums.append(1)
        dp = [[0]*(n+2) for _ in range(n+2)]

        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j: continue
                mx=0
                for k in range(i,j+1):
                    x = (nums[i-1]*nums[k]*nums[j+1]) + dp[i][k-1] + dp[k+1][j]
                    mx = max(mx,x)
                dp[i][j]=mx

        return dp[1][n]