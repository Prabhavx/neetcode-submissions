class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        lmx,rmx = 0,0
        ans = 0

        while l<r:
            if height[l] < height[r]:
                if height[l] >= lmx:
                    lmx = height[l]
                else:
                    ans += lmx-height[l]
                l+=1
            else:
                if height[r] >= rmx:
                    rmx = height[r]
                else:
                    ans += rmx-height[r]
                r-=1

        return ans
