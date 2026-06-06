from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        dist = [[float('inf')]*m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                    dist[i][j] = 0

        ans = -1
        while q:
            r, c = q.popleft()

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1):
                    grid[nr][nc] = grid[r][c] + 1
                    dist[nr][nc] = dist[r][c] + 1
                    ans = max(ans, dist[nr][nc])
                    q.append((nr, nc))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and dist[i][j] == float('inf'):
                    return -1
        ans = max(0,ans)
        return ans 
