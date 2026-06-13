from bisect import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        centre = max(0,bisect(arr, x)-1)
        if centre < n-1: 
            if abs(arr[centre]-x) > abs(arr[centre+1]-x): centre+=1
        i,j = centre, centre

        while j-i+1 < k:
            if i-1>=0 and j+1<n:
                if x - arr[i-1] <= arr[j+1] - x: i -= 1
                else: j+=1
            else:
                if i-1>0: i-=1
                else: j+=1
        
        return arr[i:j+1]

# 1 2 3 4 5
#     ^