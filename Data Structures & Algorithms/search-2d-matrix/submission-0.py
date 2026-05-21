class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        print(n,m)
        lo, hi = 0,n*m-1
        while lo<=hi:
            mid = (lo+hi)//2
            row = mid//m
            col = mid%m
            if matrix[row][col] == target: return True
            elif matrix[row][col] < target: 
                lo = mid+1
            else:
                hi = mid-1
        return False
