import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
            # construct the Graph
            n = len(points)
            G = [[] for i in range(n)]
            for point_1 in range(n):
                for point_2 in range(n):
                    if point_1 == point_2: continue
                    x1,y1 = points[point_1]
                    x2,y2 = points[point_2]
                    G[point_1].append((point_2, abs(x1-x2) + abs(y1-y2)))

            heap = [(0,0)]
            cnt = 0
            ans = 0
            vis = set()

            while heap and cnt<n:
                cost, u = heapq.heappop(heap)
                if u in vis: continue

                vis.add(u)
                ans += cost
                cnt += 1

                for v,cst in G[u]:
                    if v not in vis:
                        heapq.heappush(heap, (cst, v))
                
            return ans