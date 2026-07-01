class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        heap = [(0,0,0,heights[0][0])]
        dirs = [(0,1), (0,-1), (-1,0), (1,0)]
        ans = 0
        vis = set()

        while heap:
            diff, r, c, val = heapq.heappop(heap)
            if (r,c) in vis: continue
            vis.add((r,c))
            ans = max(ans, diff)
            if r==n-1 and c==m-1: return ans

            for dr,dc in dirs:
                nr = r+dr; nc = c+dc
                if (nr<0 or nr>n-1) or (nc<0 or nc>m-1) or (nr,nc) in vis: continue
                
                heapq.heappush(heap, (abs(val-heights[nr][nc]), nr, nc, heights[nr][nc]))
