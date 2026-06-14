from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            new = dist[:]

            for u, v, cost in flights:
                if dist[u] != float('inf'):
                    new[v] = min(new[v], dist[u] + cost)

            dist = new

        return -1 if dist[dst] == float('inf') else dist[dst]
