class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        vis = [[0]*m for _ in range(n)]

        def dfs(x,y):
            vis[x][y]=1
            if x+1<n and vis[x+1][y]==0 and grid[x+1][y]=='1': dfs(x+1, y)
            if x-1>-1 and vis[x-1][y]==0 and grid[x-1][y]=='1': dfs(x-1, y)
            if y+1<m and vis[x][y+1]==0 and grid[x][y+1]=='1': dfs(x, y+1)
            if y-1>-1 and vis[x][y-1]==0 and grid[x][y-1]=='1': dfs(x, y-1)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]=='1':
                    dfs(i,j)
                    ans += 1
        return ans
        