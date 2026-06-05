"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        g = {}
        def dfs(s):
            if s in g:
                return g[s]
            
            c = Node(s.val)
            g[s] = c

            for u in s.neighbors:
                c.neighbors.append(dfs(u))
            
            return c
        
        return dfs(node)

