import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        for i in range(n):
            a = points[i][0]
            b = points[i][1]
            points[i].insert(0, a*a + b*b)
        heapq.heapify(points)
        ans = []
        for i in range(k):
            x = heapq.heappop(points)
            ans.append([x[1],x[2]])
        return ans
