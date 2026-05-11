class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d: d[i]+=1
            else: d[i]=1
        l = [[d[i],i] for i in d]
        l.sort(reverse = True)
        l=l[:k]
        ans = [i[1] for i in l]
        return ans
        