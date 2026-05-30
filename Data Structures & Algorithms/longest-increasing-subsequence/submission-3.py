from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        le = 0
        for i in nums:
            if le>0:
                if i>dp[-1]:
                    dp.append(i)
                    le+=1
                else:
                    w = bisect_left(dp, i)
                    if w==le:
                        if dp[w-1]!=i: dp[w-1]=i
                    else:
                        if dp[w]!=i: dp[w]=i

            else:
                dp.append(i)
                le+=1

        return le

        