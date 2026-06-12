# approach

# a -4.0-> b -1.0-> c   ab -3.25-> bc
#   <-0.25-  <-1.0-        <-.3x- 

from collections import defaultdict,deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for g,x in zip(equations, values):
            a = g[0]; b = g[1]
            graph[a].append((b,x))
            graph[b].append((a,1/x))
        
        def find_path(Graph, start, target):
            if start not in Graph: return -1.0
            if start == target: return 1.0
            vis = set()
            q=deque([(start,1.0)])
            vis.add(start)
            while q:
                node, val = q.popleft()
                for vertices, cur_val in Graph[node]:
                    if vertices in vis: continue

                    if vertices == target: return val*cur_val
                    else:
                        q.append([vertices,val*cur_val])
                    vis.add(vertices)
            return -1.0

        ans = []
        for qa,qb in queries:
            ans.append(find_path(graph, qa, qb))

        return ans
            

