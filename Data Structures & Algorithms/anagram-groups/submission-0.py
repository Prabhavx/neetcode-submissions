class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang_indxs={}
        strings=[]
        for i,s in enumerate(strs):
            l=[i for i in s]            # storing string in a list to sort
            l.sort()
            sorted_s = ''.join(l)

            if sorted_s in ang_indxs:
                ang_indxs[sorted_s].append(i)
            else:
                ang_indxs[sorted_s]=[i]
        
        ans=[]
        for ang in ang_indxs:
            ang_list=[]
            for i in ang_indxs[ang]:
                ang_list.append(strs[i])
            ans.append(ang_list)
        
        return ans
            

        