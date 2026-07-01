class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for u,v in tickets[::-1]:
            graph[u].append(v)
        
        ans = []
        stk = ["JFK"]
        while stk:
            if graph[stk[-1]]:
                stk.append(graph[stk[-1]].pop())
            else:
                ans.append(stk.pop())
        return ans[::-1]

        