class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        
        vis = set()
        heap = [(0,k)]
        total = 0

        while heap:
            time,node = heapq.heappop(heap)
            if node in vis: continue
            vis.add(node)
            total = time
            
            for v,t in graph[node]:
                if v not in vis:
                    heapq.heappush(heap, (t+time,v))
        
        return total if len(vis)==n else -1

        
        