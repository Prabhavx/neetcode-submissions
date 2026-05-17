class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*(n)
        stk = [(temperatures[0],0)]
        i = 1
        while i<n:
            x = (temperatures[i],i)
            while stk and stk[-1][0] < x[0]:
                ans[stk[-1][1]] = (x[1] - stk[-1][1])
                stk.pop()
            stk.append(x)
            i+=1
        return ans