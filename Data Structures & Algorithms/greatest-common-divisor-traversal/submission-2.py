from collections import defaultdict
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if 1 in nums: return False
        
        mx = max(nums)
        spf = [0]*(mx+1)
        for i in range(2,mx+1):
            if spf[i] == 0:
                for j in range(2*i, mx+1, i):
                    if spf[j]==0: spf[j] = i
        primes = set()
        for i in nums:
            while spf[i]!=0:
                pf = spf[i]
                primes.add(pf)
                while i%pf==0: i//=pf
            if i>1: primes.add(i)

        mask = defaultdict(int)
        for i in primes:
            mask[i] = mx+1
            mx+=1
        
        adj = defaultdict(list)
        for p in primes:
            for i in nums:
                if i%p == 0: adj[i].append(mask[p]); adj[mask[p]].append(i)
        
        vis = set()
        def dfs(adj,s):
            vis.add(s)
            for u in adj[s]:
                if u not in vis: 
                    dfs(adj,u)

        dfs(adj,nums[0])
        for i in nums:
            if i not in vis: return False
        return True
