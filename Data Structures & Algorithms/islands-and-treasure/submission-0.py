from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid), len(grid[0])
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            r, c = q.popleft()

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < m and
                    grid[nr][nc] == 2147483647):

                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))