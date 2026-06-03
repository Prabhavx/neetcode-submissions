import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        projects = [[capital[i], profits[i]] for i in range(n)]
        projects.sort()
        if projects[0][0] > w: return w

        indx = n
        for i in range(n):
            if projects[i][0] > w:
                indx = i
                break
        heap = [-projects[i][1] for i in range(indx)]
        heapq.heapify(heap)

        while heap and k>0:
            w += -heapq.heappop(heap)
            while indx<n and projects[indx][0] <= w:
                heapq.heappush(heap, -projects[indx][1])
                indx += 1
            k -= 1
        return w


        
