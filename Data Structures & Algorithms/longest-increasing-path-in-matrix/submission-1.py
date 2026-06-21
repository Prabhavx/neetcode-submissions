from collections import defaultdict, deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # making the Graph
        G = defaultdict(list)
        indeg = defaultdict(int)
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if j+1<m and matrix[i][j+1] > matrix[i][j]: G[(i,j)].append((i,j+1)); indeg[(i,j+1)] += 1
                if j-1>-1 and matrix[i][j-1] > matrix[i][j]: G[(i,j)].append((i,j-1)); indeg[(i,j-1)] += 1
                if i+1<n and matrix[i+1][j] > matrix[i][j]: G[(i,j)].append((i+1,j)); indeg[(i+1,j)] += 1
                if i-1>-1 and matrix[i-1][j] > matrix[i][j]: G[(i,j)].append((i-1,j)); indeg[(i-1,j)] += 1
        
        # topologically sort the graph
        dp = defaultdict(int)
        q = deque()
        for i in range(n):
            for j in range(m):
                if indeg[(i,j)] == 0: 
                    q.append((i,j))
                    dp[(i,j)] = 1
        ans = 1
        while q:
            u = q.popleft()
            for v in G[u]:
                dp[v] = max(dp[v], 1+dp[u])
                ans = max(ans, dp[v])
                indeg[v] -= 1
                if indeg[v] == 0: q.append(v)

        return ans

        
