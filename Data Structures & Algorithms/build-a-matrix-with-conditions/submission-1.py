from collections import deque,defaultdict
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def toposort(G, k):
            indeg = [0]*(k+1)
            for u in G:
                for v in G[u]:
                    indeg[v] += 1
            
            q = deque()
            for i in range(1,k+1):
                if indeg[i] == 0: 
                    q.append(i)

            order = []
            while q:
                u = q.popleft()
                order.append(u)
                for v in G[u]:
                    if indeg[v]!=0:
                        indeg[v] -= 1
                        if indeg[v] == 0: q.append(v)
            
            return order
        
        G1 = defaultdict(list)
        G2 = defaultdict(list)
        s1,s2=set(),set()

        for i,j in rowConditions:
            G1[i].append(j)

        for i,j in colConditions:
            G2[i].append(j)
        
        ord_g1 = toposort(G1, k)
        ord_g2 = toposort(G2, k)
    
        if len(ord_g1) != k or len(ord_g2) != k: return []
        else:
            for i in range(1,k+1):
                if i not in s1: ord_g1.append(i)
            for i in range(1,k+1):
                if i not in s2: ord_g2.append(i)
            combine = {i:[0,0] for i in range(1,k+1)}

            for i in range(1,k+1): combine[ord_g1[i-1]][0] = i 
            for i in range(1,k+1): combine[ord_g2[i-1]][1] = i 

            ans = [[0]*(k) for i in range(k)]
            for i in combine:
                a,b = combine[i]
                ans[a-1][b-1] = i
            
            return ans




                

