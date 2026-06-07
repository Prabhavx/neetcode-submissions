from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]

        deg = {i:0 for i in range(n)}
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u]+=1
            deg[v]+=1
        
        leaves = deque()
        for u,x in adj.items():
            if len(x) == 1:
                leaves.append(u)
        
        while n > 2:
            sz = len(leaves)
            n -= sz

            for _ in range(sz):
                u = leaves.popleft()

                for v in adj[u]:
                    deg[v] -= 1
                    if deg[v] == 1:
                        leaves.append(v)

        return list(leaves)