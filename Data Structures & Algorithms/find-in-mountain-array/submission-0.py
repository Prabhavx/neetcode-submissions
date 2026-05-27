class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        lo, hi = 1,n-2
        peak = 0

        while lo <= hi:
            mid = (lo+hi)//2
            a,b,c = mountainArr.get(mid-1),mountainArr.get(mid),mountainArr.get(mid+1)
            if a<b>c: 
                peak = mid
                break
            elif a<b<c: lo = mid+1
            else: hi = mid-1

        lo,hi = 0,peak
        while lo <= hi:
            mid = (lo+hi)//2
            x = mountainArr.get(mid)
            if target == x: return mid
            elif target > x: lo = mid+1
            else: hi = mid-1
        
        lo,hi = peak,n-1
        while lo <= hi:
            mid = (lo+hi)//2
            x = mountainArr.get(mid)
            if target == x: return mid
            elif target > x: hi = mid-1
            else: lo = mid+1

        return -1

