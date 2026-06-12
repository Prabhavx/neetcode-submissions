class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        if left == right: return left
        while True:
            if left == 0: return ans
            x = len(bin(left)[2:])
            y = len(bin(right)[2:])
            if x==y: 
                w = pow(2,x-1)
                ans += w
                left -= w
                right -= w
            else: break
        return ans

# 1010
# 1011
# 1100