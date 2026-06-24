class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        n1 = len(nums1)
        n2 = len(nums2)

        def count_prods(x): # to count no. of pairs who product is less than x
            cnt = 0
            for num in nums1:
                if num == 0: 
                    if x >= 0: cnt += n2
                elif num > 0: cnt += bisect.bisect_right(nums2, x//num)
                elif num < 0: cnt += n2 - bisect.bisect_left(nums2, -(-x//num))
                
            return cnt
                

        lo, hi = -(10**10), (10**10)
        while lo <= hi:
            mid = (lo+hi)//2
            if count_prods(mid) < k: lo = mid + 1
            else: hi = mid - 1

        return lo       