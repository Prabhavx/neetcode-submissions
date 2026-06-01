class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)

        if abs(target) > s or (s + target) % 2:
            return 0

        req = (s + target) // 2

        dp = [0] * (req + 1)
        dp[0] = 1

        for x in nums:
            for j in range(req, x - 1, -1):
                dp[j] += dp[j - x]

        return dp[req]